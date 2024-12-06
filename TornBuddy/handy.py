from datetime import datetime

import requests
from decouple import config
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import redirect

from player.models import Player


def apiCallError(err):
    return {
        "apiError": "API error {}: {}.".format(
            err["error"]["code"], err["error"]["error"]
        ),
        "apiErrorString": err["error"]["error"],
        "apiErrorCode": int(err["error"]["code"]),
    }


def get_player(request):
    if "player" in request.session:
        player = request.session["player"]
        player = Player.objects.filter(torn_id=player)[0]
        return player
    return None


def apiCall(
    section,
    id,
    selections,
    key,
    kv={},
    sub=None,
    cache_response=False,
    cache_private=True,
):

    key = str(key)

    base_url = "https://api.torn.com/v2"

    url = f"{base_url}/{section}/{id}"

    keys_values = {
        "selections": selections,
        "key": key,
        "comment": "TORNBUDDY",
    }
    for k, v in kv.items():
        keys_values[k] = v

    url += "?" + "&".join([f"{k}={v}" for k, v in keys_values.items()])

    if cache_response:
        cache_key = f"{section}-{id}-{selections}"
        for k, v in kv.items():
            cache_key += f"-{k}{v}"
        if cache_private:
            cache_key += f"-{key}"

        # try to get cache
        r = cache.get(cache_key)

        if r is not None:
            return r

    try:
        r = requests.get(url)
    except BaseException:
        return apiCallError({"error": {"code": 0, "error": f"can't reach {base_url}"}})

    err = False

    try:
        rjson = r.json()
    except ValueError as e:
        print("API deserialization  error {}".format(e))
        err = dict(
            {
                "error": {
                    "code": 0,
                    "error": "deserialization error... API going crazy #blameched",
                }
            }
        )

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("API HTTPError {}".format(e))
        err = dict(
            {
                "error": {
                    "code": r.status_code,
                    "error": "{} #blameched".format(r.reason),
                }
            }
        )

    if not err:
        if "error" in rjson:  # standard api error
            err = rjson
        else:
            if sub is not None:
                if sub in rjson:
                    if cache_response:
                        print(f" set cache for {cache_response}s with key {cache_key}")
                        cache.set(cache_key, rjson[sub], cache_response)
                    return rjson[sub]
                else:  # key not found
                    err = dict(
                        {
                            "error": {
                                "code": 0,
                                "error": "key not found... something went wrong...",
                            }
                        }
                    )
            else:

                if cache_response:
                    print(f"set cache for {cache_response}s with key {cache_key}")
                    cache.set(cache_key, rjson, cache_response)
                return rjson

    return apiCallError(err)


def timestampToDatetime(t):
    return datetime.fromtimestamp(t)


def redirect_if_no_player(request):
    player = get_player(request=request)
    if player is None:
        messages.error(request, "You must be logged in to continue")
        return redirect("/")
    return None


def get_random_key():
    player = Player.objects.filter(valid_key=True).order_by("?").first()
    if player is not None:
        key = player.api_key
    else:
        key = config("MASTER_KEY")
    return key


def romanToInt(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i : i + 2] in roman:
            num += roman[s[i : i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num
