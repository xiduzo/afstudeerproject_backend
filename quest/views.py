from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from quest.models import Quest
from quest.serializers import QuestSerializer

# Create your views here.
class QuestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(QuestViewSet, self).get_queryset()

        return qs
