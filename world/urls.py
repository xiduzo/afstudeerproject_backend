from rest_framework import routers

from .views import (
    V2WorldViewSet,
    WorldViewSet,
    UserInWorldViewSet,
)

router = routers.DefaultRouter()
router.register(r'worlds', WorldViewSet)
router.register(r'v2-worlds', V2WorldViewSet)
router.register(r'userInWorld', UserInWorldViewSet)

urlpatterns = router.urls
