from celery import shared_task
from celery.utils.log import get_task_logger

from faction.models import Faction
from player.models import Player
from TornBuddy.handy import apiCall, get_random_key

logger = get_task_logger(__name__)


@shared_task
def faction_update_basic_info(faction_id=-1):
    if faction_id == -1:
        factions = Faction.objects.all()
        for faction in factions:
            faction_update_basic_info(faction.torn_id)
    else:
        response = apiCall("faction", faction_id, "basic", get_random_key())
        faction = Faction.objects.get_or_create(torn_id=faction_id)[0]
        faction.name = response["basic"]["name"]
        faction.tag = response["basic"]["tag"]
        faction.tag_image = response["basic"]["tag_image"]

        leader = Player.objects.get_or_create(torn_id=response["basic"]["leader_id"])[0]
        leader.save()
        # If there is not a current leader, add the one from the api response
        if not faction.leader():
            faction.add_member(leader, "Leader")
        # If the current leader is not the one from the API response, delete it and add the new leader
        elif faction.leader().player.torn_id != leader.torn_id:
            ex_lead = faction.factionmember_set.filter(player=faction.leader().player)
            ex_lead.delete()
            faction.add_member(leader, "Leader")

        leader = Player.objects.get_or_create(
            torn_id=response["basic"]["co-leader_id"]
        )[0]
        leader.save()

        # If there is not a current leader, add the one from the api response
        if not faction.co_leader():
            faction.add_member(leader, "Co-Leader")
        # If the current leader is not the one from the API response, delete it and add the new leader
        elif faction.co_leader().player.torn_id != leader.torn_id:
            ex_lead = faction.factionmember_set.filter(player=faction.leader().player)
            ex_lead.delete()
            faction.add_member(leader, "Co-Leader")

        # TODO: Player -  update self or other in background
        # TODO: Coleader - update self or other in background

        faction.respect = response["basic"]["respect"]
        faction.days_old = response["basic"]["days_old"]
        faction.capacity = response["basic"]["capacity"]
        faction.members = response["basic"]["members"]
        faction.enlisted = response["basic"]["is_enlisted"]
        faction.rank_level = response["basic"]["rank"]["level"]
        faction.rank_name = response["basic"]["rank"]["name"]
        faction.rank_division = response["basic"]["rank"]["division"]
        faction.rank_position = response["basic"]["rank"]["position"]
        faction.rank_wins = response["basic"]["rank"]["wins"]
        faction.best_chain = response["basic"]["best_chain"]
        faction.save()
