from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from world.models import World
from world.serializers import WorldSerializer, WorldOverviewSerializer

# Create your views here.
class WorldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(WorldViewSet, self).get_queryset()

        return qs
        

class WorldOverviewSet(viewsets.ReadOnlyModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldOverviewSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(WorldOverviewSet, self).get_queryset()

        return qs
