from django.db import models

from player.models import Player


# Create your models here.
class Faction(models.Model):
    torn_id = models.IntegerField(null=False)
    name = models.CharField(null=True)
    tag = models.CharField(null=True)
    tag_image = models.CharField(null=True)
    leader = models.ForeignKey(
        Player, on_delete=models.PROTECT, null=True, related_name="leader"
    )
    co_leader = models.ForeignKey(
        Player, on_delete=models.PROTECT, null=True, related_name="co_leader"
    )
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
