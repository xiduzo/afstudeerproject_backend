from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Rule(UUIDModel):
    RULE__TYPES = (
        (1, 'houding'),
        (2, 'functioneren binnen het team'),
        (3, 'kennisontwikkeling'),
        (4, 'verantwoording'),
    )

    rule = models.TextField(blank=False, null=False)
    rule_eng = models.TextField(blank=False, null=False)
    points = models.IntegerField(blank=False, null=False)

    rule_type = models.CharField(max_length=2, choices=RULE__TYPES)
