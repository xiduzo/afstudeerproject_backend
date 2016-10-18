from rest_framework import routers

from .views import (
    GuildViewSet,
    GuildRuleViewSet,
    GuildRuleEndorsmentViewSet,
    NewGuildRuleEndorsmentViewSet,
    UserInGuildViewSet,
    GuildQuestViewSet,
    GuildObjectiveViewSet,
    GuildHistoryUpdateViewSet,
    GuildFullHistoryUpdateViewSet,
    GuildObjectiveAssignmentViewSet,
    NewGuildViewSet,
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet, base_name='guilds')
router.register(r'newGuild', NewGuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)
router.register(r'guildObjective', GuildObjectiveViewSet)
router.register(r'guildObjectiveAssignment', GuildObjectiveAssignmentViewSet)
router.register(r'guildHistory', GuildHistoryUpdateViewSet)
router.register(r'guildFullHistory', GuildFullHistoryUpdateViewSet)
router.register(r'guildRules', GuildRuleViewSet)
router.register(r'guildRulesEndorsments', GuildRuleEndorsmentViewSet, base_name='endorsements')
router.register(r'newGuildRulesEndorsments', NewGuildRuleEndorsmentViewSet)

urlpatterns = router.urls
