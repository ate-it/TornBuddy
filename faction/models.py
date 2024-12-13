import logging

from django.db import models

from player.models import Player
from TornBuddy.handy import apiCall
from TornBuddy.models import TimeStampedModel

logger = logging.getLogger("TornBuddy")


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
        logging.info(f"Added {player.torn_id} to {self.torn_id} as {role}")
        member = FactionMember(
            faction=self, player=player, role=role, days_in_faction=days_in_faction
        )
        member.save()

    def delete_member(self, player):
        print(2)

    def update_members(self):
        # Grab a key from any db_members_with_key
        db_members = self.factionmember_set.filter(faction_id=self.id).all()
        db_members_with_key = (
            db_members.all().exclude(player__valid_key=False).order_by("?").first()
        )
        key = db_members_with_key.player.api_key

        # Get a list of members from API
        response = apiCall("faction", "", "members", key)
        members = response["members"]
        print(members)
        # TODO if response contains members

        # TODO: if there are members in the DB that are not in the API delete them
        # TODO: get or update existing members
        print(2)


class FactionMember(models.Model):
    def __str__(self):
        return f"[{self.faction.torn_id}] {self.faction.name} - [{self.player.torn_id}] {self.player.name} - {self.role}"

    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.CharField(null=True)
    days_in_faction = models.IntegerField(default=-1)
