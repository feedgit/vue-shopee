import time, random, os
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.hero.models import Hero
from apps.equipment.models import Equipment

class UserEquipment(models.Model):
    user = models.ForeignKey(User, related_name='user_equipments', on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, related_name='user_who_owned_equipment', on_delete=models.CASCADE)

    bought_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' bought ' + self.equipment.name

class UserHero(models.Model):
    user = models.ForeignKey(User, related_name='user_heroes', on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, related_name='user_who_owned_hero', on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    bought_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' bought ' + self.hero.name
