from rest_framework import routers

from .views import (
    BehaviourViewset,
    RewardViewset,
    BehaviourRupeeRewardViewset,
    RewardRupeeCostViewset,
)

router = routers.DefaultRouter()
router.register(r'behaviour', BehaviourViewset)
router.register(r'reward', RewardViewset)
router.register(r'behaviourReward', BehaviourRupeeRewardViewset)
router.register(r'rewardCost', RewardRupeeCostViewset)

urlpatterns = router.urls
