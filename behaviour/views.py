from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)

from rest_framework.renderers import JSONRenderer

from .models import (
    Behaviour,
    Reward,
    BehaviourRupeeReward,
    RewardRupeeCost,
)
from .serializers import (
    BehaviourSerializer,
    RewardSerializer,
    BehaviourRupeeRewardSerializer,
    RewardRupeeCostSerializer,
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
    renderer_classes = (JSONRenderer)

    def get_queryset(self):
        qs = super(RewardViewset, self).get_queryset()

        return qs

class BehaviourRupeeRewardViewset(viewsets.ModelViewSet):
    queryset = BehaviourRupeeReward.objects.all()
    serializer_class = BehaviourRupeeRewardSerializer

    def get_queryset(self):
        qs = super(BehaviourRupeeRewardViewset, self).get_queryset()

        return qs

class RewardRupeeCostViewset(viewsets.ModelViewSet):
    queryset = RewardRupeeCost.objects.all()
    serializer_class = RewardRupeeCostSerializer

    def get_queryset(self):
        qs = super(RewardRupeeCostViewset, self).get_queryset()

        return qs
