from TornBuddy.handy import redirect_if_no_player


def index(request):
    response = redirect_if_no_player(request=request)
    if response:
        return response
