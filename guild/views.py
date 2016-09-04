from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from guild.models import (
    Guild,
    UserInGuild,
    GuildQuest,
    GuildObjective,
    GuildHistoryUpdate,
)
from guild.serializers import (
    GuildSerializer,
    UserInGuildSerializer,
    GuildQuestSerializer,
    GuildObjectiveSerializer,
    GuildHistoryUpdateSerializer,
)

# Create your views here.
class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(GuildViewSet, self).get_queryset()

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
        qs = super(GuildHistoryUpdateViewSet, self).get_queryset()

        return qs
