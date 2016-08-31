from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Guild, UserInGuild
)

from user.models import User
from world.models import World
from guild.models import (
    Guild,
    UserInGuild,
    GuildQuest,
    GuildObjective,
)
from quest.models import Quest, QuestObjective

from user.serializers import UserSerializer, PlainUserSerializer
from quest.serializers import PlainQuestSerializer

class GuildObjectiveSerializer(serializers.ModelSerializer):

    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )

    class Meta:
        model = GuildObjective
        fields = (
            'id',
            'guild',
            'name',
            'objective',
            'points',
            'completed',
            'completed_by',
            'completed_at',
        )

class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = User.objects.filter(guilds__guild=obj)
        return PlainUserSerializer(instance=users, many=True, context=self.context).data

    members = serializers.SerializerMethodField()
    objectives = GuildObjectiveSerializer(many=True, read_only=True)

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
            'members',
            'objectives',
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
            'completed',
        )
