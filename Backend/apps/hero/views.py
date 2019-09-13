from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'slug'
    # filterset_fields = ('type_id', )
    # filter_backends = (DjangoFilterBackend, )
