from rest_framework import routers

from .views import (
    QuestViewSet
)

router = routers.DefaultRouter()
router.register(r'quests', QuestViewSet)

urlpatterns = router.urls
