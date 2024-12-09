import logging

from decouple import config
from django.db import models
from django.utils import timezone

from player.models import Player
from TornBuddy.handy import apiCall, romanToInt, timestampToDatetime

logger = logging.getLogger("TornBuddy")


class NPC(models.Model):

    def __str__(self):
        return f"[{self.torn_id}] {self.name}"

    torn_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, default="?")
    status = models.TextField(max_length=20, default="Ok")
    loot_level = models.IntegerField(default="0")
    last_hospital = models.IntegerField(null=True, default=28377016)
    last_update = models.IntegerField(null=True, default=28377016)
    visible = models.BooleanField(default=False)

    def last_update_datetime(self):

        return (
            timestampToDatetime(self.last_update).strftime("%d/%m/%Y %H:%M:%S") + " TCT"
        )

    def in_hospital(self):
        return self.status == "hospitalized"

    def update(self):
        logger.info(f"DEBUG: Updating loot for {self.name}")
        player = Player.objects.filter(valid_key=True).order_by("?").first()
        if player is not None:
            key = player.api_key
        else:
            key = config("MASTER_KEY")
        req = apiCall("user", self.torn_id, "profile,timestamp", key=key)

        if "apiError" in req:
            return req["apiError"]
        else:

            self.name = req.get("name", "?")
            self.last_update = req.get("timestamp")

            states = req.get("states")
            status = req.get("status")

            if states["hospital_timestamp"] != 0:
                self.last_hospital = states["hospital_timestamp"]
                self.status = "hospitalized"
            else:
                self.status = status["details"]
                self.loot_level = romanToInt(
                    status["details"].replace("Loot level ", "")
                )
            self.save()

    def lootTimings(self, lvl=None):
        now = int(timezone.now().timestamp())
        lootTimings = dict({0: {"lvl": 0}})
        # ts = [self.hospitalTS,  # lvl 1
        #       self.hospitalTS + 30 * 60,  # lvl 2
        #       self.hospitalTS + 90 * 60,  # lvl 3
        #       self.hospitalTS + 210 * 60,  # lvl 4
        #       self.hospitalTS + 450 * 60,  # lvl 5
        #       ]

        add = 0
        next = 0
        for i in range(5):
            add = 2 * add + min(i, 1) * 30
            ts = self.last_hospital + add * 60
            due = ts - now
            if due > 0:
                next += 1

            if next == 0:
                pro = 100
            elif next == 1:
                if add:
                    pro = 100 * (1.0 - max(due, 0) / float(add * 60))
                else:
                    pro = 100 * (1.0 - max(due, 0) / float(120 * 60))
            else:
                pro = 0

            lootTimings[i + 1] = {
                "lvl": i + 1,
                "ts": timestampToDatetime(ts).strftime("%d/%m/%Y %H:%M:%S"),
                "due": due,
                "pro": int(pro),
                "next": next,
            }

        current = 5 - lootTimings[5]["next"]

        if lvl is None:
            return lootTimings
        elif lvl in ["next"]:
            return lootTimings[min(current + 1, 5)]
        elif lvl in ["current"]:
            return lootTimings[current]
        else:
            return lootTimings[lvl]
