from rest_framework import serializers

from .models import NPC


class LootSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = "__all__"
