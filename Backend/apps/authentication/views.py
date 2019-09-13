from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, exceptions, status
from rest_framework.response import Response
from apps.account.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

@api_view(['POST'])
def register(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        password = request.data.get('password', None)
        if password is None:
            raise exceptions.ValidationError("Password is required")
        user = User.objects.create(**request.data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
