from rest_framework import routers

from .views import (
    UserViewSet,
    UserWorldsViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userWorlds', UserWorldsViewSet, base_name="userWorlds")

urlpatterns = router.urls
