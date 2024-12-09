from django.shortcuts import render

from TornBuddy.handy import get_player, redirect_if_no_player


def index(request):
    response = redirect_if_no_player(request=request)
    if response:
        return response

    player = get_player(request=request)
    # factions = query to get factions to which player has access
    factions = []

    context = {"factions": factions, "player": player}
    return render(request, "faction/index.html", context)
