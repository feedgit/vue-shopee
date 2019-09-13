from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, exceptions, status
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_heroes(request):
    qs = UserHero.objects.all()
    return Response(UserHeroSerializer(qs, many=True, context={'request': request}).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_equipments(request):
    qs = UserEquipment.objects.all()
    return Response(UserEquipmentSerializer(qs, many=True, context={'request': request}).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def buy_hero(request):
    hero_id = request.data.get('hero_id', None)
    UserHero.objects.create(user=request.user, hero_id=hero_id)
    return Response({ success: True }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def buy_equipment(request):
    equipment_id = request.data.get('equipment_id', None)
    UserEquipment.objects.create(user=request.user, equipment_id=equipment_id)
    return Response({ success: True }, status=status.HTTP_200_OK)
