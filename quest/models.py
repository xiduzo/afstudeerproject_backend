from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from libs.models import UUIDModel
from tinymce.models import HTMLField

# Create your models here.
class Quest(UUIDModel):
    name = models.CharField(max_length=200)
    description = HTMLField()
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
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(
            self.name,
        )

class QuestObjective(UUIDModel):
    quest = models.ForeignKey('quest.Quest', related_name='objectives')

    name = models.CharField(max_length=250)
    objective = HTMLField()
    points = models.PositiveIntegerField()

    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(
            self.name,
        )
