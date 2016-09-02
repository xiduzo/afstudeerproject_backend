from rest_framework import routers

from .views import (
    GuildViewSet,
    UserInGuildViewSet,
    GuildQuestViewSet,
    GuildObjectiveViewSet,
    GuildHistoryUpdateViewSet,
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)
router.register(r'guildObjective', GuildObjectiveViewSet)
router.register(r'guildHistory', GuildHistoryUpdateViewSet)

urlpatterns = router.urls
