from rest_framework import routers

from .views import (
    V2GuildMembersViewSet,
    V2GuildRulesViewSet,

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
# V2
router.register(r'members', V2GuildMembersViewSet, base_name='members')
router.register(r'rules', V2GuildRulesViewSet, base_name='rules')


# Legacy
router.register(r'guilds', GuildViewSet, base_name='guilds')
router.register(r'newGuild', NewGuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)
router.register(r'guildRules', GuildRuleViewSet)
router.register(r'guildRulesEndorsments', GuildRuleEndorsmentViewSet, base_name='endorsements')
router.register(r'newGuildRulesEndorsments', NewGuildRuleEndorsmentViewSet)
router.register(r'userGuildRupees', UserGuildRupeesViewSet)

urlpatterns = router.urls
