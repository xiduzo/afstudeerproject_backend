from rest_framework import serializers

from .models import (
    World,
    UserInWorld,
)

from guild.models import (
    Guild
)

from guild.serializers import GuildSerializer
from user.serializers import UserSerializer, GamemasterSerializer
from user.models import User

class V2UserInWorldSerializer(serializers.ModelSerializer):
    user = GamemasterSerializer()

    class Meta:
        model = UserInWorld
        fields = (
            'id',
            'user'
        )

class V2WorldGuildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'name',
        )

class V2WorldSerializer(serializers.ModelSerializer):
    gamemasters = V2UserInWorldSerializer(many=True,read_only=True)
    guilds = V2WorldGuildSerializer(many=True,read_only=True)

    class Meta:
        model = World
        depth = 1
        fields = (
            'url',
            'id',
            'name',
            'course_duration',
            'start',
            'trello_user_id',
            'gamemasters',
            'guilds'
        )

class WorldSerializer(serializers.ModelSerializer):
    guilds = GuildSerializer(many=True, read_only=True)

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
            'id',
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
