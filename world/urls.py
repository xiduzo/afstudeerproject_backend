from rest_framework import routers

from .views import (
    WorldViewSet,
    UserInWorldViewSet,
    WorldRuleViewSet,
)

router = routers.DefaultRouter()
router.register(r'worlds', WorldViewSet)
router.register(r'userInWorld', UserInWorldViewSet)
router.register(r'worldRule', WorldRuleViewSet)

urlpatterns = router.urls
