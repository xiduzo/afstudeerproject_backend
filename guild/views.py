from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status,
    permissions
)
from guild.models import (
    Guild,
    GuildRule,
    GuildRuleEndorsment,
    UserInGuild,
    UserGuildRupees,
    GuildQuest,
)

from guild.serializers import (
    V2GuildMembersSerializer,
    V2GuildRulesSerializer,

    GuildSerializer,
    GuildRuleSerializer,
    GuildRuleEndorsmentSerializer,
    NewGuildRuleEndorsmentSerializer,
    UserInGuildSerializer,
    UserGuildRupeesSerializer,
    GuildQuestSerializer,
    NewGuildSerializer,
)


#V2
class V2GuildMembersViewSet(viewsets.ModelViewSet):
    queryset = UserInGuild.objects.all()
    serializer_class = V2GuildMembersSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        qs = super(V2GuildMembersViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild)

        return qs

class V2GuildRulesViewSet(viewsets.ModelViewSet):
    queryset = GuildRule.objects.all()
    serializer_class = V2GuildRulesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        qs = super(V2GuildRulesViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild)

        return qs


# Legagy
class GuildRuleViewSet(viewsets.ModelViewSet):
    queryset = GuildRule.objects.all()
    serializer_class = GuildRuleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(GuildRuleViewSet, self).get_queryset()

        return qs

class GuildRuleEndorsmentViewSet(viewsets.ModelViewSet):
    queryset = GuildRuleEndorsment.objects.all()
    serializer_class = GuildRuleEndorsmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(GuildRuleEndorsmentViewSet, self).get_queryset()

        return qs

class NewGuildRuleEndorsmentViewSet(viewsets.ModelViewSet):
    queryset = GuildRuleEndorsment.objects.all()
    serializer_class = NewGuildRuleEndorsmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(NewGuildRuleEndorsmentViewSet, self).get_queryset()

        return qs

# Create your views here.
class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(GuildViewSet, self).get_queryset()

        return qs

class NewGuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = NewGuildSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(NewGuildViewSet, self).get_queryset()

        return qs

class UserInGuildViewSet(viewsets.ModelViewSet):
    queryset = UserInGuild.objects.all()
    serializer_class = UserInGuildSerializer
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(UserGuildRupeesViewSet, self).get_queryset()

        return qs


class GuildQuestViewSet(viewsets.ModelViewSet):
    queryset = GuildQuest.objects.all()
    serializer_class = GuildQuestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        guild = self.request.query_params.get('guild')
        quest = self.request.query_params.get('quest')
        qs = super(GuildQuestViewSet, self).get_queryset()

        if guild:
            qs = qs.filter(guild=guild)
        if quest:
            qs = qs.filter(quest=quest)

        return qs
