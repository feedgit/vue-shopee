from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

@api_view(['GET'])
def get_homepage_data(request):
    # from apps.footballer.models import Footballer
    # from apps.footballer.serializers import FootballerSerializer
    # fb_qs = Footballer.objects.all()[:30]
    # footballer_data = FootballerSerializer(fb_qs, many=True, context={'request': request}).data
    #
    # from apps.club.models import Club
    # clb_qs = Club.objects.all()[:10]
    # clb_data = FootballerSerializer(clb_qs, many=True, context={'request': request}).data

    return Response(1, status=status.HTTP_200_OK)
