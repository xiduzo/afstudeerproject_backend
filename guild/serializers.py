from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Guild, UserInGuild
)

from user.models import User
from user.serializers import UserSerializer, PlainUserSerializer
from quest.serializers import QuestSerializer

from world.models import World
from guild.models import Guild, UserInGuild, GuildQuest
from quest.models import Quest

class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = User.objects.filter(guilds__guild=obj)
        return PlainUserSerializer(instance=users, many=True, context=self.context).data

    def get_quests(self, obj):
        quests = Quest.objects.filter(guilds__guild=obj)
        return QuestSerializer(instance=quests, many=True, context=self.context).data

    quests = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    world = serializers.PrimaryKeyRelatedField(
        read_only=True
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
            'quests',
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
            'world',
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
    guild = GuildSerializer()
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

class GuildQuestSerializer(serializers.ModelSerializer):
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    quest = serializers.HyperlinkedRelatedField(
        view_name='quest-detail',
        queryset=Quest.objects.all(),
    )

    class Meta:
        model = GuildQuest
        fields = (
            'url',
            'guild',
            'quest',
            'completed'
        )
