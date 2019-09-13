from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    order_by = '-created_at'
    lookup_field = 'slug'
