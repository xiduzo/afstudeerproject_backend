from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Behaviour(UUIDModel):
    BEHAVIOUR__TYPES = (
        (1, 'individual behaviour'),
        (2, 'group behaviour'),
    )

    behaviour = models.TextField(blank=False, null=False)
    behaviour_type = models.CharField(max_length=2, choices=BEHAVIOUR__TYPES)
    points = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(
            self.behaviour,
        )

class Reward(UUIDModel):
    REWARD__TYPES = (
        (1, 'individual behaviour'),
        (2, 'group behaviour'),
    )

    reward = models.TextField(blank=True)
    reward_type = models.CharField(max_length=2, choices=REWARD__TYPES)
    points = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(
            self.reward,
        )

class BehaviourRupeeReward(UUIDModel):
    RUPEE__TYPES = (
        (1, 'ruby'),
        (2, 'sapphire'),
        (3, 'emerald'),
        (4, 'amethyst'),
    )

    behaviour = models.ForeignKey('behaviour.Behaviour', related_name='rupees')
    rupee = models.CharField(max_length=2, choices=RUPEE__TYPES)
    amount = models.IntegerField(blank=False, null=False)

class RewardRupeeCost(UUIDModel):
    RUPEE__TYPES = (
        (1, 'ruby'),
        (2, 'sapphire'),
        (3, 'emerald'),
        (4, 'amethyst'),
    )

    reward = models.ForeignKey('behaviour.Reward', related_name='rupees')
    rupee = models.CharField(max_length=2, choices=RUPEE__TYPES)
    amount = models.IntegerField(blank=False, null=False)
