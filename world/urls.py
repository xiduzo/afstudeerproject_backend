from rest_framework import routers

from .views import (
    WorldViewSet,
    UserInWorldViewSet,
)

router = routers.DefaultRouter()
router.register(r'worlds', WorldViewSet)
router.register(r'userInWorld', UserInWorldViewSet)

urlpatterns = router.urls
