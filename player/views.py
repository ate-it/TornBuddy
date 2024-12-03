from django.contrib import messages
from django.shortcuts import render

from TornBuddy.handy import apiCall, get_player

from .models import Player


# Create your views here.
def login(request):
    if get_player(request):
        return render(request, "dashboard/index.html")

    if request.method == "GET":
        return render(request, "player/login.html")

    elif request.method == "POST":
        response = apiCall("user", "", "", request.POST["api_key"])
        if "apiError" in response:
            messages.error(request, response["apiErrorString"])
            return render(request, "player/login.html")
        else:

            player = Player.objects.get_or_create(torn_id=response["player_id"])[0]
            player.api_key = request.POST["api_key"]
            player.save()

            player = player.update_own_key()

            request.session["player"] = player.torn_id

            messages.error(request, "Welcome!")
            return render(request, "dashboard/index.html", {"player": player})


def logout(request):
    del request.session["player"]
    messages.error(request, "BYEEEE!")
    return render(request, "dashboard/index.html")
