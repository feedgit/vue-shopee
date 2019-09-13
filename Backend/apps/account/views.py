from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    order_by = '-created_at'
    lookup_field = 'id'

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_account_information(request):
    user = request.user
    return Response({
        'id': user.id,
        'name': user.name,
        'avatar': request.build_absolute_uri(user.avatar.url) if user.avatar else None,
        'coin': user.coin
    }, status=status.HTTP_200_OK)
