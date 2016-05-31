from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from libs.models import UUIDModel

# Create your models here.
class Quest(UUIDModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    experience = models.PositiveIntegerField()
    interaction_design = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    visual_interface_design = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    frontend_development = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    content_management = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    project_management = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    world = models.ForeignKey('world.World', related_name='quests')
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(
            self.name,
        )
