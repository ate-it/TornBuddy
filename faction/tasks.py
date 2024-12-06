from celery import shared_task
from celery.utils.log import get_task_logger

from faction.models import Faction
from player.models import Player
from TornBuddy.handy import apiCall, get_random_key

logger = get_task_logger(__name__)


@shared_task
def faction_update_basic_info(faction_id):
    response = apiCall("faction", faction_id, "basic", get_random_key())
    faction = Faction.objects.get_or_create(torn_id=faction_id)[0]
    faction.name = response["basic"]["name"]
    faction.tag = response["basic"]["tag"]
    faction.tag_image = response["basic"]["tag_image"]
    player = Player.objects.get_or_create(torn_id=response["basic"]["leader_id"])[0]
    faction.leader = player
    # TODO: Player -  update self or other in background
    # TODO: Coleader - get_or_create and update self or other

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
