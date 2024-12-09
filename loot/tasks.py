# tasks.py

import logging

from celery import shared_task

from loot.models import NPC

logger = logging.getLogger("TornBuddy")


@shared_task
def update_loot_npc():
    logger.info("Starting Loot Update")
    NPCs = NPC.objects.all()
    for npc in NPCs:
        npc.update()
    logger.info("Ending Loot Update")
    return True
