from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Guild(UUIDModel):
    name = models.CharField( max_length=100)

    world = models.ForeignKey('world.World', related_name='guilds')

    def __str__(self):
        return self.name

class UserInGuild(UUIDModel):
    user = models.ForeignKey('user.User', related_name='guilds')
    guild = models.ForeignKey('guild.Guild', related_name='users')

    def __str__(self):
        return '{} in {}'.format(
            self.user,
            self.guild,
        )
