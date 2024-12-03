from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from loot.models import NPC
from TornBuddy.handy import get_player

from .serializers import LootSerializer


def index(request):

    NPCs = NPC.objects.filter(visible=True).order_by("name")
    player = get_player(request=request)
    context = {"NPCs": NPCs, "player": player}
    return render(request, "loot/index.html", context)


class LootApiView(APIView):
    """
    Returns all NPC's with loot timer information
    """

    @swagger_auto_schema(
        operation_description="Returns NPC Loot Details",
        operation_summary="Returns NPC Loot Details",
    )
    def get(self, request, *args, **kwargs):
        queryset = NPC.objects.all()
        serializer = LootSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
