from rest_framework import serializers
from .models import *
from apps.account_item.models import UserHero

class HeroSerializer(serializers.ModelSerializer):
    request_owned = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = '__all__'

    def get_request_owned(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        return UserHero.objects.filter(user=request.user, hero=obj).exists()
