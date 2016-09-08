from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    User,
)

from world.models import World, UserInWorld


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'uid',
            'student_number',
            'email',
            'initials',
            'first_name',
            'surname_prefix',
            'surname',
            'gender',
            'is_staff',
            'is_superuser',
        )

class PlainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'uid',
            'email',
            'first_name',
            'surname_prefix',
            'surname',
        )

class GamemasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'email',
            'initials',
            'first_name',
            'surname',
        )
