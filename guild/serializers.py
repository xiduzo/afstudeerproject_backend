from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Guild, UserInGuild
)

from user.models import User
from user.serializers import UserSerializer, PlainUserSerializer

from world.models import World
from guild.models import Guild, UserInGuild

class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = User.objects.filter(guilds__guild=obj)
        return PlainUserSerializer(instance=users, many=True, context=self.context).data

    members = serializers.SerializerMethodField()

    world = serializers.HyperlinkedRelatedField(
        view_name='world-detail',
        queryset=World.objects.all(),
    )

    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'name',
            'world',
            'members',
        )

class PlainGuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'name',
        )

class UserInGuildSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all(),
    )
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    class Meta:
        model = UserInGuild
        fields = (
            'url',
            'user',
            'guild',
        )

class UserGuild(serializers.ModelSerializer):
    guild = PlainGuildSerializer()
    class Meta:
        model = UserInGuild
        fields = (
            'url',
            'guild',
        )

class UserGuildsSerializer(serializers.ModelSerializer):
    def get_guilds(self, obj):
        guilds = UserInGuild.objects.filter(user=obj)
        return UserGuild(instance=guilds, many=True, context=self.context).data

    guilds = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'guilds',
        )
