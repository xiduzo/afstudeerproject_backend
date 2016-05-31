from rest_framework import routers

from .views import (
    GuildViewSet
)

router = routers.DefaultRouter()
router.register(r'guilds', GuildViewSet)

urlpatterns = router.urls
