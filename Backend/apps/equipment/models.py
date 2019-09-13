import time, random, os
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.urls import reverse
from conf.storage import OverwriteStorage

class Equipment(models.Model):

    def upload_equipment_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(100000, 99999999)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(randomInt) + ext
        return "%s/%s" %("equipments/", file_name)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    thumbnail = models.FileField("Uploaded thumbnail of equipment", storage=OverwriteStorage(), upload_to=upload_equipment_path, blank=True, null=True)
    price = models.BigIntegerField(default=0)

    physical_damage = models.IntegerField(default=0)
    magic_damage = models.IntegerField(default=0)
    physical_defence = models.IntegerField(default=0)
    magic_defence = models.IntegerField(default=0)
    attack_to_heal = models.IntegerField(default=0) # Per attack turn

    plus_health = models.IntegerField(default=500)
    plus_mana = models.IntegerField(default=400)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
