from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Behaviour,
    Reward,
)


class BehaviourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behaviour
        fields = (
            'url',
            'id',
            'behaviour',
            'behaviour_type',
            'points',
        )

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = (
            'url',
            'id',
            'reward',
            'reward_type',
            'points',
        )
