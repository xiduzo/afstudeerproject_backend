from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Quest,
)

from world.models import World

class QuestSerializer(serializers.ModelSerializer):
    world = serializers.HyperlinkedRelatedField(
        view_name='world-detail',
        queryset=World.objects.all(),
    )
    class Meta:
        model = Quest
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'world',
            'name',
            'description',
            'experience',
            'interaction_design',
            'visual_interface_design',
            'frontend_development',
            'content_management',
            'project_management',
            'active',
        )
