from rest_framework import routers

from .views import (
    UserViewSet,
    UserWorldsViewSet,
    UserGuildsViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userWorlds', UserWorldsViewSet, base_name="userWorlds")
router.register(r'userGuilds', UserGuildsViewSet, base_name="userGuilds")

urlpatterns = router.urls
