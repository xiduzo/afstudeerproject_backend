from django.db import models

from libs.models import UUIDModel

# Create your models here.
class Quest(UUIDModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    experience = models.PositiveIntegerField()
    interaction_design = models.PositiveIntegerField()
    visual_interface_design = models.PositiveIntegerField()
    frontend_development = models.PositiveIntegerField()
    content_management = models.PositiveIntegerField()
    project_management = models.PositiveIntegerField()
    world = models.ForeignKey('world.World', related_name='quests')
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(
            self.name,
        )
