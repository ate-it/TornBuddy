from django.db import models


class NPC(models.Model):
    torn_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20, default="?")
    status = models.TextField(max_length=20, default="Ok")
    loot_level = models.IntegerField
    last_hospital = models.DateTimeField
    last_update = models.DateTimeField
    visible = models.BooleanField(default=False)

    def update(self, key):
        print(2)
        # FIXME: key = random key pluck
        # TODO: get user info
        # TODO: update user info
