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
    V2UserWorldsSerializer,
)

from world.models import (
    World,
    UserInWorld,
)

from world.serializers import (
    WorldSerializer,
    UserWorldsSerializer,
)

from guild.serializers import (
    UserGuildsSerializer,
)

# V2
class V2UserWorldsViewSet(viewsets.ModelViewSet):
    queryset = UserInWorld.objects.all()
    serializer_class = V2UserWorldsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(V2UserWorldsViewSet, self).get_queryset()
        user = self.request.query_params.get('user')

        if user:
            qs = qs.filter(user=user)

        return qs

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        uid = self.request.query_params.get('uid')
        email = self.request.query_params.get('email')
        student_number = self.request.query_params.get('student_number')
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

        if student_number:
            qs = qs.filter(student_number=student_number)

        return qs

class UserWorldsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWorldsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(UserWorldsViewSet, self).get_queryset()

        return qs

class UserGuildsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserGuildsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super(UserGuildsViewSet, self).get_queryset()

        return qs
