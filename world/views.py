from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from world.models import World
from world.serializers import WorldSerializer

# Create your views here.
class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(WorldViewSet, self).get_queryset()

        return qs
