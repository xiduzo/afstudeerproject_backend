from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Guild, UserInGuild
)

from user.models import User
from user.serializers import UserSerializer, PlainUserSerializer

class GuildSerializer(serializers.HyperlinkedModelSerializer):
    def get_members(self, obj):
        users = User.objects.filter(guilds__guild=obj)
        return PlainUserSerializer(instance=users, many=True, context=self.context).data

    members = serializers.SerializerMethodField()

    class Meta:
        model = Guild
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'name',
            'members'
        )
