from rest_framework import serializers
from django.utils.translation import gettext as _

from .models import (
    Behaviour,
    Reward,
    BehaviourRupeeReward,
    RewardRupeeCost,
)

class BehaviourRupeeRewardSerializer(serializers.ModelSerializer):
    behaviour = serializers.HyperlinkedRelatedField(
        view_name='behaviour-detail',
        queryset=Behaviour.objects.all(),
    )
    class Meta:
        model = BehaviourRupeeReward
        fields = (
            'url',
            'id',
            'behaviour',
            'rupee',
            'amount'
        )

class BehaviourSerializer(serializers.ModelSerializer):
    def get_rewards(self, obj):
        behaviour = BehaviourRupeeReward.objects.filter(behaviour=obj)
        return BehaviourRupeeRewardSerializer(instance=behaviour, many=True, context=self.context).data

    rewards = serializers.SerializerMethodField()

    class Meta:
        model = Behaviour
        fields = (
            'url',
            'id',
            'behaviour',
            'behaviour_type',
            'points',
            'rewards',
        )

class RewardRupeeCostSerializer(serializers.ModelSerializer):
    reward = serializers.HyperlinkedRelatedField(
        view_name='reward-detail',
        queryset=Reward.objects.all(),
    )
    class Meta:
        model = RewardRupeeCost
        fields = (
            'url',
            'id',
            'reward',
            'rupee',
            'amount'
        )

class RewardSerializer(serializers.ModelSerializer):
    # def get_cost(self, obj):
    #     reward = RewardRupeeCost.objects.filter(reward=obj)
    #     return RewardRupeeCostSerializer(instance=reward, many=True, context=self.context).data
    #
    # cost = serializers.SerializerMethodField()

    class Meta:
        model = Reward
        fields = (
            'url',
            'id',
            # 'reward',
            'reward_type',
            'points',
            # 'cost'
        )
