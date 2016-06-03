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
)
from guild.serializers import (
    GuildSerializer,
    UserInGuildSerializer,
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
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        user = self.request.query_params.get('user')
        guild = self.request.query_params.get('guild')
        qs = super(UserInGuildViewSet, self).get_queryset()

        if user and guild:
            qs = qs.filter(user=user, guild=guild)

        return qs
