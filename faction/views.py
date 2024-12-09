from django.shortcuts import render

from faction.models import FactionMember
from TornBuddy.handy import get_player, redirect_if_no_player


def index(request):
    response = redirect_if_no_player(request=request)
    if response:
        return response

    player = get_player(request=request)

    # TODO: If a player has been granted access to a faction, add it to the list
    factions = []
    # If player is a member of a faction, add it to the list
    member_of = FactionMember.objects.filter(player=player).first()
    factions.append(member_of.faction)
    # TODO: If there is only one faction, redirect to the view of this
    context = {"factions": factions, "player": player}
    return render(request, "faction/index.html", context)
