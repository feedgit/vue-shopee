from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ('is_active', 'is_staff', 'password', 'last_login', 'groups', 'user_permissions')
