from django.contrib import messages
from django.shortcuts import redirect, render

from faction.models import Faction, FactionMember
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

    if len(factions) == 1:

        return redirect(f"/faction/{factions[0].torn_id}")
    else:
        context = {"factions": factions, "player": player}
        return render(request, "faction/index.html", context)


def view_faction(request, faction_id):
    response = redirect_if_no_player(request=request)
    if response:
        return response

    player = get_player(request=request)
    faction = Faction.objects.filter(torn_id=faction_id).first()

    if not faction or not player.can_access_faction(faction):
        messages.error(request, "Now why are you poking around here?")
        return render(request, "dashboard/index.html")
    else:
        # TODO: Update if not updated in x
        context = {"faction": faction, "player": player}
        return render(request, "faction/view.html", context)


def faction_members(request, faction_id):
    response = redirect_if_no_player(request=request)
    if response:
        return response

    player = get_player(request=request)
    faction = Faction.objects.filter(torn_id=faction_id).first()

    if not faction or not player.can_access_faction(faction):
        messages.error(request, "Now why are you poking around here?")
        return render(request, "dashboard/index.html")
    else:
        # TODO: only update members if it's been longer than x
        members = faction.update_members()
        context = {"faction": faction, "members": members, "player": player}
        return render(request, "faction/view.html", context)
