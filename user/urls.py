from rest_framework import routers

from .views import (
    UserViewSet,
    UserWorldsViewSet,
    UserGuildsViewSet,
    V2UserWorldsViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'worlds', V2UserWorldsViewSet, base_name="v2-worlds")
router.register(r'userWorlds', UserWorldsViewSet, base_name="userWorlds")
router.register(r'userGuilds', UserGuildsViewSet, base_name="userGuilds")

urlpatterns = router.urls
