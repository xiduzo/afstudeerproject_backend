from rest_framework import routers

from .views import (
    GuildViewSet,
    UserInGuildViewSet
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet)
router.register(r'userInGuild', UserInGuildViewSet)

urlpatterns = router.urls
