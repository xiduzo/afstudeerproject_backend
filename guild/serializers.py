from rest_framework import serializers

from .models import (
    Guild, UserInGuild
)

from user.models import User
from world.models import (
    World,
)
from guild.models import (
    Guild,
    GuildRule,
    GuildRuleEndorsment,
    UserInGuild,
    UserGuildRupees,
    GuildQuest,
)

from quest.models import Quest, QuestObjective

from user.serializers import (
    UserSerializer,
    PlainUserSerializer,
    GamemasterSerializer,
)

from quest.serializers import QuestSerializer, PlainQuestSerializer
# from world.serializers import V2PlainWorldSerializer


# V2
class V2GuildMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInGuild
        fields = (
            'id',
            'user',
            'guild'
        )

class V2GuildRulesSerializer(serializers.ModelSerializer):

    guild = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = GuildRule
        depth = 1
        fields = (
            'id',
            'rule',
            'rule_eng',
            'rule_type',
            'points',
            'guild',
            'endorsements',
        )

class V2PlainWorldSerializer(serializers.ModelSerializer):

    class Meta:
        model = World
        fields = (
            'url',
            'id',
            'name',
            'start',
            'course_duration',
            'trello_user_id'
        )

class GuildSerializer(serializers.ModelSerializer):
    def get_members(self, obj):
        users = UserInGuild.objects.filter(guild=obj)
        return UserInGuildFullSerializer(instance=users, many=True, context=self.context).data


    members = serializers.SerializerMethodField()
    world = V2PlainWorldSerializer()

    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'created_at',
            'name',
            'trello_board',
            'trello_done_list',
            'trello_legenda_list',
            'members',
            'rules',
            'world'
        )

# Legacy
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
            'rule_eng',
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
            'rule_eng',
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
            'rating',
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
            'rating'
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
            'id',
            'url',
            'guild',
            'user',
        )

class UserInGuildFullSerializer(serializers.ModelSerializer):
    def get_rupees(self, obj):
        user_in_guild = UserGuildRupees.objects.filter(user_in_guild=obj)
        return UserGuildRupeesSerializer(instance=user_in_guild, many=True, context=self.context).data

    user = UserSerializer()
    guild = serializers.HyperlinkedRelatedField(
        view_name='guild-detail',
        queryset=Guild.objects.all(),
    )
    class Meta:
        model = UserInGuild
        fields = (
            'id',
            'url',
            'user',
            'guild',
        )

class PlainGuildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'trello_board',
            'trello_done_list',
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
