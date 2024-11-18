from django.shortcuts import render

from loot.models import NPC
from loot.tasks import update_loot_npc


def index(request):
    NPCs = NPC.objects.filter(visible=True)
    # TODO: Only run this if data is x old
    # TODO: live update view
    for npc in NPCs:
        update_loot_npc.delay(npc.torn_id)
    context = {"NPCs": NPCs}
    return render(request, "loot/index.html", context)
