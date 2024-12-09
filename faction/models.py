from django.db import models

from player.models import Player


# Create your models here.
class Faction(models.Model):

    def __str__(self):
        return f"[{self.torn_id}] {self.name}"

    torn_id = models.IntegerField(null=False)
    name = models.CharField(null=True)
    tag = models.CharField(null=True)
    tag_image = models.CharField(null=True)

    respect = models.IntegerField(default=-1)
    days_old = models.IntegerField(default=-1)
    capacity = models.IntegerField(default=-1)
    members = models.IntegerField(default=-1)
    enlisted = models.BooleanField(default=False)
    rank_level = models.IntegerField(default=-1)
    rank_name = models.CharField(null=True)
    rank_division = models.IntegerField(default=-1)
    rank_position = models.IntegerField(default=-1)
    rank_wins = models.IntegerField(default=-1)
    best_chain = models.IntegerField(default=-1)


class FactionMember(models.Model):
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    role = models.CharField(null=True)
    days_in_faction = models.IntegerField(default=-1)
