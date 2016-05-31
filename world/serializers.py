from rest_framework import serializers

from .models import (
    World,
)

from guild.serializers import GuildSerializer
from quest.serializers import QuestSerializer
from user.serializers import UserSerializer
from user.models import User


class WorldSerializer(serializers.ModelSerializer):
    guilds = GuildSerializer(many=True, read_only=True)
    quests = QuestSerializer(many=True, read_only=True)

    def get_gamemasters(self, obj):
        gamemasters = User.objects.filter(worlds__world=obj)
        return UserSerializer(instance=gamemasters, many=True, context=self.context).data

    gamemasters = serializers.SerializerMethodField()

    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'name',
            'guilds',
            'quests',
            'gamemasters'
        )
