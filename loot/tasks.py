# tasks.py

from celery import shared_task
from celery.utils.log import get_task_logger

from loot.models import NPC

logger = get_task_logger(__name__)


@shared_task
def update_loot_npc():
    print("Debug: Starting Loot Update")
    NPCs = NPC.objects.all()
    for npc in NPCs:
        npc.update()
    print("Debug: Ending Loot Update")
    return True
