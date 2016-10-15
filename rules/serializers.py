from rest_framework import serializers
from django.db.models import Sum

from .models import (
    Rule,
)

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = (
            'id',
            'rule',
            'points',
            'rule_type',
        )
