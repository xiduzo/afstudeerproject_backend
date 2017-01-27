from rest_framework import routers

from .views import (
    GuildViewSet,
    GuildRuleViewSet,
    GuildRuleEndorsmentViewSet,
    NewGuildRuleEndorsmentViewSet,
    UserInGuildViewSet,
    GuildQuestViewSet,
    NewGuildViewSet,
    UserGuildRupeesViewSet,
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet, base_name='guilds')
router.register(r'newGuild', NewGuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)
router.register(r'guildRules', GuildRuleViewSet)
router.register(r'guildRulesEndorsments', GuildRuleEndorsmentViewSet, base_name='endorsements')
router.register(r'newGuildRulesEndorsments', NewGuildRuleEndorsmentViewSet)
router.register(r'userGuildRupees', UserGuildRupeesViewSet)

urlpatterns = router.urls
