from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Guild(UUIDModel):
    name = models.CharField( max_length=100)

    world = models.ForeignKey('world.World', related_name='guilds')

    accepted_rules = models.BooleanField(default=False)

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

class GuildQuest(UUIDModel):
    guild = models.ForeignKey('guild.Guild', related_name='quests')
    quest = models.ForeignKey('quest.Quest', related_name='guilds')

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    grade = models.PositiveIntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return '{} for {}'.format(
            self.quest.name,
            self.guild.name
        )

class GuildObjective(UUIDModel):
    guild = models.ForeignKey('guild.Guild', related_name='objectives')

    name = models.CharField(max_length=250)
    objective = models.TextField(blank=True, null=True)
    points = models.PositiveIntegerField()

    completed = models.BooleanField(default=False)
    completed_by = models.ForeignKey('user.User', related_name='users', null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(
            self.name,
        )

class GuildObjectiveAssignment(UUIDModel):
    objective = models.ForeignKey('guild.GuildObjective', related_name='assignments')
    user = models.ForeignKey('user.User', related_name='user_objectives')

    def __str__(self):
        return '{} assigned to {}'.format(
            self.user.first_name,
            self.objective.name
        )

class GuildHistoryUpdate(UUIDModel):
    ACTION__TYPES = (
        (1, 'added task'),
        (2, 'removed task'),
        (3, 'assigned'),
        (4, 'remove assigned'),
        (5, 'completed'),
        (6, 'remove completed'),
        (7, 'graded'),
        (8, 'regraded'),
        (9, 'completed assessment'),
        (10, 'remove completed assessment'),
    )

    guild = models.ForeignKey('guild.Guild', related_name='history_updates')
    user = models.ForeignKey('user.User', related_name='persons')

    action = models.TextField(blank=False, null=False)
    action_type = models.CharField(max_length=2, choices=ACTION__TYPES)

    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(
            self.user.name,
            self.action
        )

class GuildRule(UUIDModel):
    RULE__TYPES = (
        (1, 'houding'),
        (2, 'functioneren binnen het team'),
        (3, 'kennisontwikkeling'),
        (4, 'verantwoording'),
    )

    guild = models.ForeignKey('guild.Guild', related_name='rules')
    rule = models.TextField(blank=False, null=False)
    points = models.IntegerField(blank=False, null=False)

    rule_type = models.CharField(max_length=2, choices=RULE__TYPES)
