from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status,
    permissions
)
from world.models import (
    World,
    UserInWorld,
)

from world.serializers import (
    V2WorldSerializer,
    WorldSerializer,
    UserInWorldSerializer,
)

# Create your views here.

class V2WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = V2WorldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(V2WorldViewSet, self).get_queryset()

        return qs

class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(WorldViewSet, self).get_queryset()

        return qs

class UserInWorldViewSet(viewsets.ModelViewSet):
    queryset = UserInWorld.objects.all()
    serializer_class = UserInWorldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        user = self.request.query_params.get('user')
        world = self.request.query_params.get('world')
        qs = super(UserInWorldViewSet, self).get_queryset()

        if user and world:
            qs = qs.filter(user=user, world=world)

        return qs
