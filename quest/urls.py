from rest_framework import routers

from .views import (
    QuestViewSet,
    QuestObjectiveViewSet
)

router = routers.DefaultRouter()
router.register(r'quests', QuestViewSet)
router.register(r'objectives', QuestObjectiveViewSet)

urlpatterns = router.urls
