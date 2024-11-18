import datetime

from django.shortcuts import render

from loot.models import NPC
from loot.tasks import update_loot_npc


def index(request):
    NPCs = NPC.objects.filter(visible=True).order_by("name")

    # TODO: live update view
    context = {"NPCs": NPCs}
    time_ago = (datetime.datetime.now() - datetime.timedelta(minutes=10)).timestamp()
    for npc in NPCs:
        if npc.last_update > time_ago:
            update_loot_npc(npc.torn_id)

    return render(request, "loot/index.html", context)
