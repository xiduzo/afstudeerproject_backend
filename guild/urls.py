from rest_framework import routers

from .views import (
    GuildViewSet,
    UserInGuildViewSet,
    GuildQuestViewSet,
    GuildObjectiveViewSet,
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)
router.register(r'guildObjective', GuildObjectiveViewSet)

urlpatterns = router.urls
