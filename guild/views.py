from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from guild.models import Guild
from guild.serializers import GuildSerializer

# Create your views here.
class GuildViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(GuildViewSet, self).get_queryset()

        return qs
