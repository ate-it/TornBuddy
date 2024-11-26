from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from loot.models import NPC

from .serializers import LootSerializer


def index(request):

    NPCs = NPC.objects.filter(visible=True).order_by("name")
    context = {"NPCs": NPCs}
    return render(request, "loot/index.html", context)


class LootApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = NPC.objects.all()
        serializer = LootSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
