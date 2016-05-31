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
            'id',
            'created_at',
            'modified_at',
            'name',
            'description',
            'experience',
            'interaction_design',
            'visual_interface_design',
            'frontend_development',
            'content_management',
            'project_management',
            'world',
            'active',
        )
