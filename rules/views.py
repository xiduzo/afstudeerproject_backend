from django.shortcuts import render
from rest_framework import (
    viewsets,
    response,
    mixins,
    status
)

from .models import (
    Rule
)

from .serializers import (
    RuleSerializer,
)

# Create your views here.
class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def get_queryset(self):
        qs = super(RuleViewSet, self).get_queryset()

        return qs