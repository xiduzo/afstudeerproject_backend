from rest_framework import serializers
from django.db.models import Sum

from .models import (
    World,
    UserInWorld,
)

from quest.models import Quest

from guild.serializers import GuildSerializer
from quest.serializers import QuestSerializer
from user.serializers import UserSerializer, GamemasterSerializer
from user.models import User

class WorldSerializer(serializers.ModelSerializer):
    guilds = GuildSerializer(many=True, read_only=True)
    quests = QuestSerializer(many=True, read_only=True)

    def get_gamemasters(self, obj):
        gamemasters = User.objects.filter(worlds__world=obj)
        return GamemasterSerializer(instance=gamemasters, many=True, context=self.context).data

    gamemasters = serializers.SerializerMethodField()

    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'created_at',
            'name',
            'course_duration',
            'start',
            'gamemasters',
            'quests',
            'guilds',
        )

class PlainWorldSerializer(serializers.ModelSerializer):
    guilds = GuildSerializer(many=True, read_only=True)
    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'name',
            'guilds'
        )

class OnlyWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'name'
        )

class UserInWorldSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all(),
    )
    world = serializers.HyperlinkedRelatedField(
        view_name='world-detail',
        queryset=World.objects.all(),
    )
    class Meta:
        model = UserInWorld
        fields = (
            'url',
            'user',
            'world',
        )

class UserWorld(serializers.ModelSerializer):
    world = PlainWorldSerializer()
    class Meta:
        model = UserInWorld
        fields = (
            'url',
            'world',
        )

class UserWorldsSerializer(serializers.ModelSerializer):
    def get_worlds(self, obj):
        worlds = UserInWorld.objects.filter(user=obj)
        return UserWorld(instance=worlds, many=True, context=self.context).data

    worlds = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'worlds',
        )
