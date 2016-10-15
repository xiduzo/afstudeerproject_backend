from django.db import models
from libs.models import UUIDModel

# Create your models here.
class World(UUIDModel):
    name = models.CharField(max_length=150)
    course_duration = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserInWorld(UUIDModel):
    user = models.ForeignKey('user.User', related_name='worlds')
    world = models.ForeignKey('world.World', related_name='gamemasters')

    def __str__(self):
        return '{} in {}'.format(
            self.user,
            self.world,
        )
