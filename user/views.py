from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status,
    permissions
)
from user.models import User
from user.serializers import (
    UserSerializer,
)

from world.models import World
from world.serializers import (
    WorldSerializer,
    UserWorldsSerializer,
)

from guild.serializers import (
    UserGuildsSerializer,
)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        uid = self.request.query_params.get('uid')
        email = self.request.query_params.get('email')
        is_staff = self.request.query_params.get('is_staff')
        is_superuser = self.request.query_params.get('is_superuser')
        qs = super(UserViewSet, self).get_queryset()

        if uid:
            qs = qs.filter(uid=uid)

        if email:
            qs = qs.filter(email=email)

        if is_staff:
            qs = qs.filter(is_staff=is_staff)

        if is_superuser:
            qs = qs.filter(is_superuser=is_superuser)

        return qs

class UserWorldsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWorldsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(UserWorldsViewSet, self).get_queryset()

        return qs

class UserGuildsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserGuildsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(UserGuildsViewSet, self).get_queryset()

        return qs
