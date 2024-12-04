from django.shortcuts import render

from TornBuddy.handy import get_player


def index(request):
    player = get_player(request=request)
    return render(request, "dashboard/index.html", {"player": player})
