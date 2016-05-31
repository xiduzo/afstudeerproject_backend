from rest_framework import routers

from .views import (
    WorldViewSet, WorldOverviewSet
)

router = routers.DefaultRouter()
router.register(r'all', WorldViewSet)
router.register(r'overview', WorldOverviewSet)

urlpatterns = router.urls
