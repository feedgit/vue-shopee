from rest_framework import serializers
from .models import *

class UserEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserEquipment
        fields = '__all__'

class UserHeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserHero
        fields = '__all__'
