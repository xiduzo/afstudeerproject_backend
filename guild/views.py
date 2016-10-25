from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
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
from guild.serializers import (
    GuildSerializer,
    GuildRuleSerializer,
    GuildRuleEndorsmentSerializer,
    NewGuildRuleEndorsmentSerializer,
    UserInGuildSerializer,
    UserGuildRupeesSerializer,
    GuildQuestSerializer,
    GuildObjectiveSerializer,
    GuildHistoryUpdateSerializer,
    GuildFullHistoryUpdateSerializer,
    GuildFullObjectiveAssignmentSerializer,
    NewGuildSerializer,
)

class GuildRuleViewSet(viewsets.ModelViewSet):
    queryset = GuildRule.objects.all()
    serializer_class = GuildRuleSerializer

    def get_queryset(self):
        qs = super(GuildRuleViewSet, self).get_queryset()

        return qs

class GuildRuleEndorsmentViewSet(viewsets.ModelViewSet):
    queryset = GuildRuleEndorsment.objects.all()
    serializer_class = GuildRuleEndorsmentSerializer

    def get_queryset(self):
        qs = super(GuildRuleEndorsmentViewSet, self).get_queryset()

        return qs

class NewGuildRuleEndorsmentViewSet(viewsets.ModelViewSet):
    queryset = GuildRuleEndorsment.objects.all()
    serializer_class = NewGuildRuleEndorsmentSerializer

    def get_queryset(self):
        qs = super(NewGuildRuleEndorsmentViewSet, self).get_queryset()

        return qs

# Create your views here.
class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(GuildViewSet, self).get_queryset()

        return qs

class NewGuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = NewGuildSerializer

    def get_queryset(self):
        qs = super(NewGuildViewSet, self).get_queryset()

        return qs

class UserInGuildViewSet(viewsets.ModelViewSet):
    queryset = UserInGuild.objects.all()
    serializer_class = UserInGuildSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        guild = self.request.query_params.get('guild')
        qs = super(UserInGuildViewSet, self).get_queryset()

        if user and guild:
            qs = qs.filter(user=user, guild=guild)

        return qs

class UserGuildRupeesViewSet(viewsets.ModelViewSet):
    queryset = UserGuildRupees.objects.all()
    serializer_class = UserGuildRupeesSerializer

    def get_queryset(self):
        qs = super(UserGuildRupeesViewSet, self).get_queryset()

        return qs


class GuildQuestViewSet(viewsets.ModelViewSet):
    queryset = GuildQuest.objects.all()
    serializer_class = GuildQuestSerializer

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        quest = self.request.query_params.get('quest')
        qs = super(GuildQuestViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild)
        if quest:
            qs = qs.filter(quest=quest)

        return qs

class GuildObjectiveViewSet(viewsets.ModelViewSet):
    queryset = GuildObjective.objects.all()
    serializer_class = GuildObjectiveSerializer

    def get_queryset(self):
        qs = super(GuildObjectiveViewSet, self).get_queryset()

        return qs

class GuildHistoryUpdateViewSet(viewsets.ModelViewSet):
    queryset = GuildHistoryUpdate.objects.all()

    serializer_class = GuildHistoryUpdateSerializer

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        qs = super(GuildHistoryUpdateViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild)

        return qs

class GuildFullHistoryUpdateViewSet(viewsets.ModelViewSet):
    queryset = GuildHistoryUpdate.objects.all()

    serializer_class = GuildFullHistoryUpdateSerializer

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        start = int(self.request.query_params.get('start'))
        qs = super(GuildFullHistoryUpdateViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild).order_by("-created_at")

        if start:
            return qs[start:start+25]
        return qs

class GuildObjectiveAssignmentViewSet(viewsets.ModelViewSet):
    queryset = GuildObjectiveAssignment.objects.all()
    serializer_class = GuildFullObjectiveAssignmentSerializer

    def get_queryset(self):
        qs = super(GuildObjectiveAssignmentViewSet, self).get_queryset()

        return qs
