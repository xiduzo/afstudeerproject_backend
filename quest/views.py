from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)
from quest.models import Quest, QuestObjective
from quest.serializers import QuestSerializer, QuestObjectiveSerializer

# Create your views here.
class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    # authentication_classes = (authentication.SessionAuthentication,)

    def get_queryset(self):
        qs = super(QuestViewSet, self).get_queryset()

        return qs

class QuestObjectiveViewSet(viewsets.ModelViewSet):
    queryset = QuestObjective.objects.all()
    serializer_class = QuestObjectiveSerializer

    def get_queryset(self):
        qs = super(QuestObjectiveViewSet, self).get_queryset()

        return qs
