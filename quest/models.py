from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from libs.models import UUIDModel
from tinymce.models import HTMLField

# Create your models here.
class Quest(UUIDModel):
    moodle_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200)
    description = HTMLField()
    experience = models.PositiveIntegerField()
    interaction_design = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    visual_design = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    techniek = IntegerField(
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

    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(
            self.name,
        )
