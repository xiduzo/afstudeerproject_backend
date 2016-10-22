from rest_framework import routers

from .views import (
    BehaviourViewset,
    RewardViewset,
)

router = routers.DefaultRouter()
router.register(r'behaviour', BehaviourViewset)
router.register(r'reward', RewardViewset)

urlpatterns = router.urls
