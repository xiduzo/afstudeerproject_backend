from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)

from .models import (
    Behaviour,
    Reward,
)
from .serializers import (
    BehaviourSerializer,
    RewardSerializer,
)

class BehaviourViewset(viewsets.ModelViewSet):
    queryset = Behaviour.objects.all()
    serializer_class = BehaviourSerializer

    def get_queryset(self):
        qs = super(BehaviourViewset, self).get_queryset()

        return qs

class RewardViewset(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    def get_queryset(self):
        qs = super(RewardViewset, self).get_queryset()

        return qs
