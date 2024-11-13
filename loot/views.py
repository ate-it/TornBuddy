from django.shortcuts import render

from loot.models import NPC


def index(request):
    NPCs = NPC.objects.filter(visible=True)
    # TODO: Only run this if data is x old
    # TODO: Run in backround and live update view
    for npc in NPCs:
        npc.update()
    context = {"NPCs": NPCs}
    return render(request, "loot/index.html", context)
