from decouple import config
from django.db import models

from TornBuddy.handy import apiCall, romanToInt, timestampToDatetime


class NPC(models.Model):
    torn_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, default="?")
    status = models.TextField(max_length=20, default="Ok")
    loot_level = models.IntegerField(default="0")
    last_hospital = models.IntegerField(null=True)
    last_update = models.IntegerField(null=True)
    visible = models.BooleanField(default=False)

    def last_update_datetime(self):

        return timestampToDatetime(self.last_update).strftime("%d/%m/%Y, %H:%M:%S")

    def update(self):

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
