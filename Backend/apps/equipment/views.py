from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    order_by = '-created_at'
    lookup_field = 'id'
