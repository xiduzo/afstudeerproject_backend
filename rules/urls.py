from rest_framework import routers

from .views import (
    RuleViewSet,
)

router = routers.DefaultRouter()
router.register(r'rules', RuleViewSet)

urlpatterns = router.urls
