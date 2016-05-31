from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Quest,
)


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = (
            'url',
            'created_at',
            'modified_at',
            'name',
        )
