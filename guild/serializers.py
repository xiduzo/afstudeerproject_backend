from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Guild, UserInGuild
)

from user.models import User
from world.models import World
from guild.models import (
    Guild,
    GuildRule,
    GuildRuleEndorsment,
    UserInGuild,
    UserGuildRupees,
    GuildQuest,
    GuildObjective,
    GuildHistoryUpdate,
    GuildObjectiveAssignment,
)
from quest.models import Quest, QuestObjective

from user.serializers import UserSerializer, PlainUserSerializer
from quest.serializers import QuestSerializer, PlainQuestSerializer
# from world.serializers import OnlyWorldSerializer

class GuildRuleSerializer(serializers.ModelSerializer):
    def get_endorsements(self, obj):
        endorsements = GuildRuleEndorsment.objects.filter(rule=obj)
        return GuildRuleEndorsmentSerializer(instance=endorsements, many=True, context=self.context).data

    endorsements = serializers.SerializerMethodField()

    class Meta:
        model = GuildRule
        fields = (
            'url',
            'id',
            'guild',
            'rule',
            'rule_type',
            'points',
            'endorsements',
        )

class PlainGuildRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildRule
        fields = (
            'url',
            'id',
            'guild',
            'rule',
            'rule_type',
            'points',
        )

class GuildRuleEndorsmentSerializer(serializers.ModelSerializer):
    rule = PlainGuildRuleSerializer()
    class Meta:
        model = GuildRuleEndorsment
        fields = (
            'id',
            'rule',
            'user',
            'endorsed_by',
            'week',
        )

class NewGuildRuleEndorsmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildRuleEndorsment
        fields = (
            'id',
            'rule',
            'user',
            'endorsed_by',
            'week',
        )

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
            'about',
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
            'about',
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

class UserGuildRupeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGuildRupees
        fields = (
            'id',
            'user_in_guild',
            'rupee',
            'amount',
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
            'guild',
            'user',
        )

class UserInGuildFullSerializer(serializers.ModelSerializer):
    def get_rupees(self, obj):
        user_in_guild = UserGuildRupees.objects.filter(user_in_guild=obj)
        return UserGuildRupeesSerializer(instance=user_in_guild, many=True, context=self.context).data

    rupees = serializers.SerializerMethodField()

    user = UserSerializer()
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
            'rupees',
        )


class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = UserInGuild.objects.filter(guild=obj)
        return UserInGuildFullSerializer(instance=users, many=True, context=self.context).data

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
    rules = GuildRuleSerializer(many=True, read_only=True);

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
            'rules',
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
