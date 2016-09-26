from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Quest,
    QuestObjective,
)

from world.models import World

class QuestObjectiveSerializer(serializers.ModelSerializer):

    quest = serializers.HyperlinkedRelatedField(
        view_name='quest-detail',
        queryset=Quest.objects.all(),
    )

    class Meta:
        model = QuestObjective
        fields = (
            'id',
            'url',
            'quest',
            'created_at',
            'name',
            'objective',
            'completed',
        )

class QuestSerializer(serializers.ModelSerializer):
    world = serializers.HyperlinkedRelatedField(
        view_name='world-detail',
        queryset=World.objects.all(),
    )

    objectives = QuestObjectiveSerializer(many=True, read_only=True)

    class Meta:
        model = Quest
        fields = (
            'url',
            'id',
            'moodle_link',
            'created_at',
            'modified_at',
            'world',
            'name',
            'description',
            'experience',
            'interaction_design',
            'visual_design',
            'techniek',
            'active',
            'objectives',
        )

class PlainQuestSerializer(serializers.ModelSerializer):

    objectives = QuestObjectiveSerializer(many=True, read_only=True)

    class Meta:
        model = Quest
        fields = (
            'url',
            'id',
            'created_at',
            'modified_at',
            'name',
            'objectives',
        )
