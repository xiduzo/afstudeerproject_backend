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
    GuildHistoryUpdate,
    GuildObjectiveAssignment,
)
from quest.models import Quest, QuestObjective

from user.serializers import UserSerializer, PlainUserSerializer
from quest.serializers import QuestSerializer, PlainQuestSerializer
# from world.serializers import OnlyWorldSerializer

class NewGuildSerializer(serializers.ModelSerializer):
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
        )

class OnlyWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'name'
        )

class GuildHistoryUpdateSerializer(serializers.ModelSerializer):
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all(),
    )

    class Meta:
        model = GuildHistoryUpdate
        fields = (
            'id',
            'created_at',
            'user',
            'guild',
            'action',
            'action_type',
        )

class GuildFullHistoryUpdateSerializer(serializers.ModelSerializer):
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    user = UserSerializer()

    class Meta:
        model = GuildHistoryUpdate
        fields = (
            'id',
            'created_at',
            'user',
            'guild',
            'action',
            'action_type',
        )

class GuildFullObjectiveAssignmentSerializer(serializers.ModelSerializer):
    objective = serializers.HyperlinkedRelatedField(
        view_name='guildobjective-detail',
        queryset=GuildObjective.objects.all(),
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all(),
    )

    class Meta:
        model = GuildObjectiveAssignment
        fields = (
            'id',
            'objective',
            'user',
        )

class GuildObjectiveAssignmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GuildObjectiveAssignment
        fields = (
            'id',
            'user',
        )

class GuildObjectiveSerializer(serializers.ModelSerializer):

    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )

    assignments = GuildObjectiveAssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = GuildObjective
        fields = (
            'url',
            'id',
            'created_at',
            'guild',
            'name',
            'objective',
            'points',
            'completed',
            'assignments',
            'completed_by',
            'completed_at',
        )

class GuildFullQuestSerializer(serializers.ModelSerializer):
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    quest = QuestSerializer();

    class Meta:
        model = GuildQuest
        fields = (
            'id',
            'url',
            'guild',
            'quest',
            'completed',
            'grade',
        )

class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = User.objects.filter(guilds__guild=obj)
        return PlainUserSerializer(instance=users, many=True, context=self.context).data

    def get_history_updates(self, obj):
        history_updates = GuildHistoryUpdate.objects.filter(guild=obj)
        history_updates = history_updates.order_by("-created_at")[:50]
        return GuildFullHistoryUpdateSerializer(
                instance=history_updates,
                many=True,
                context=self.context
            ).data

    members = serializers.SerializerMethodField()
    objectives = GuildObjectiveSerializer(many=True, read_only=True)
    history_updates = serializers.SerializerMethodField()
    quests = GuildFullQuestSerializer(many=True, read_only=True);

    world = OnlyWorldSerializer()

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
            'history_updates',
            'quests',
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
            'grade',
        )
