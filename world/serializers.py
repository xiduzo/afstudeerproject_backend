from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    World,
)

from guild.serializers import GuildSerializer
from quest.serializers import QuestSerializer
from user.serializers import UserSerializer
from user.models import User


class WorldSerializer(serializers.HyperlinkedModelSerializer):
    guilds = GuildSerializer(many=True)
    quests = QuestSerializer(many=True)

    def get_gamemasters(self, obj):
        gamemasters = User.objects.filter(worlds__world=obj)
        return UserSerializer(instance=gamemasters, many=True, context=self.context).data

    gamemasters = serializers.SerializerMethodField()

    class Meta:
        model = World
        fields = (
            'url',
            'created_at',
            'modified_at',
            'name',
            'guilds',
            'quests',
            'gamemasters'
        )

class WorldOverviewSerializer(serializers.HyperlinkedModelSerializer):
    def get_gamemasters(self, obj):
        gamemasters = User.objects.filter(worlds__world=obj)
        return UserSerializer(instance=gamemasters, many=True, context=self.context).data

    gamemasters = serializers.SerializerMethodField()

    class Meta:
        model = World
        fields = (
            'url',
            'name',
            'gamemasters'
        )
