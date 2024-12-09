from django.db import models

from player.models import Player
from TornBuddy.models import TimeStampedModel


# Create your models here.
class Faction(TimeStampedModel):

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

    def leader(self):
        return self.factionmember_set.filter(role="Leader").first()

    def co_leader(self):
        return self.factionmember_set.filter(role="Co-Leader").first()

    def add_member(self, player, role, days_in_faction=0):
        member = FactionMember(
            faction=self, player=player, role=role, days_in_faction=days_in_faction
        )
        member.save()

    def delete_member(self, player):
        print(2)


class FactionMember(models.Model):
    def __str__(self):
        return f"[{self.faction.torn_id}] {self.faction.name} - [{self.player.torn_id}] {self.player.name} - {self.role}"

    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.CharField(null=True)
    days_in_faction = models.IntegerField(default=-1)
