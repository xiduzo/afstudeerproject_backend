from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    User,
)

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
            'surname',
            'gender',
            'is_staff',
            'is_superuser'
        )
