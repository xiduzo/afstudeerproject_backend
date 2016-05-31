from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from user.models import User
from user.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        uid = self.request.query_params.get('uid')
        qs = super(UserViewSet, self).get_queryset()

        if uid:
            qs = qs.filter(uid=uid)

        return qs
