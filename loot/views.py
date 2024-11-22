from django.shortcuts import render

from loot.models import NPC


def index(request):

    NPCs = NPC.objects.filter(visible=True).order_by("name")
    context = {"NPCs": NPCs}
    return render(request, "loot/index.html", context)
