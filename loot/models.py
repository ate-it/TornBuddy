from django.db import models

from TornBuddy.handy import apiCall, romanToInt


class NPC(models.Model):
    torn_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, default="?")
    status = models.TextField(max_length=20, default="Ok")
    loot_level = models.IntegerField
    last_hospital = models.DateTimeField
    last_update = models.DateTimeField
    visible = models.BooleanField(default=False)

    def update(self):

        key = "4NCRzvFCTehQNoTC"  # FIXME: Key
        req = apiCall("user", self.torn_id, "profile,timestamp", key=key)

        if "apiError" in req:
            return req["apiError"]
        else:

            self.name = req.get("name", "?")
            self.last_update = req.get("timestamp")

            states = req.get("states")
            status = req.get("status")

            self.loot_level = romanToInt(status["details"].replace("Loot level ", ""))
            if states["hospital_timestamp"] != 0:
                self.last_hospital = states["hospital_timestamp"]
                self.status = "hospitalized"
            else:
                self.status = status["details"]
            self.save()
