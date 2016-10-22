from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Behaviour(UUIDModel):
    BEHAVIOUR__TYPES = (
        (1, 'individual behaviour'),
        (2, 'group behaviour'),
    )

    behaviour = models.TextField(blank=False, null=False )
    behaviour_type = models.CharField(max_length=2, choices=BEHAVIOUR__TYPES)
    points = models.PositiveIntegerField(blank=False, null=False)

class Reward(UUIDModel):
    REWARD__TYPES = (
        (1, 'individual behaviour'),
        (2, 'group behaviour'),
    )

    reward = models.TextField(blank=True)
    reward_type = models.CharField(max_length=2, choices=REWARD__TYPES)
    points = models.PositiveIntegerField(blank=True, null=True)
