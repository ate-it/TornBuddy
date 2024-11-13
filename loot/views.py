from django.shortcuts import render

from loot.models import NPC


def index(request):
    NPCs = NPC.objects.filter(visible=True)
    return render(request, "loot/index.html", NPCs)
