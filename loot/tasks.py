# tasks.py

from celery import shared_task

from loot.models import NPC


@shared_task
def update_loot_npc(torn_id):
    # Task logic here
    npc = NPC.objects.get(torn_id=torn_id)
    npc.update()
    return True
