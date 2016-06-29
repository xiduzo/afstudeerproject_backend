from rest_framework import routers

from .views import (
    GuildViewSet,
    UserInGuildViewSet,
    GuildQuestViewSet,
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)
router.register(r'guildQuest', GuildQuestViewSet)

urlpatterns = router.urls
