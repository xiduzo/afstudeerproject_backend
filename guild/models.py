from django.db import models
from libs.models import UUIDModel

# Create your models here.
class Guild(UUIDModel):
    name = models.CharField( max_length=100)

    world = models.ForeignKey('world.World', related_name='guilds')
    trello_board = models.TextField(blank=True, null=True)
    trello_done_list = models.TextField(blank=True, null=True)
    trello_legenda_list = models.TextField(blank=True, null=True)

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

class UserGuildRupees(UUIDModel):
    RUPEE__TYPES = (
        (1, 'ruby'),
        (2, 'sapphire'),
        (3, 'emerald'),
        (4, 'amethyst'),
    )

    user_in_guild = models.ForeignKey('guild.UserInGuild', related_name='rupees')
    rupee = models.CharField(max_length=2, choices=RUPEE__TYPES)
    amount = models.IntegerField(blank=False, null=False)

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

class GuildRule(UUIDModel):
    RULE__TYPES = (
        (1, 'houding'),
        (2, 'functioneren binnen het team'),
        (3, 'kennisontwikkeling'),
        (4, 'verantwoording'),
    )

    guild = models.ForeignKey('guild.Guild', related_name='rules')
    rule = models.TextField(blank=False, null=False)
    rule_eng = models.TextField(blank=False, null=False)
    points = models.IntegerField(blank=False, null=False)

    rule_type = models.CharField(max_length=2, choices=RULE__TYPES)

    # Getting unicode error, this is a temp. fix
    # def __str__(self):
    #     return '{}: {}'.format(
    #         self.guild.name,
    #         self.rule
    #     )

class GuildRuleEndorsment(UUIDModel):
    rule = models.ForeignKey('guild.GuildRule', related_name='endorsements')
    user = models.ForeignKey('user.User', related_name="endorsed")
    endorsed_by = models.ForeignKey('user.User', related_name="endorser", null= True, blank=True)
    week = models.IntegerField(blank=False, null=False)
    rating = models.PositiveIntegerField(blank=False, null=False, default=0)
