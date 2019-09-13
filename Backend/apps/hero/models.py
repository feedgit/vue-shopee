import time, random, os
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.urls import reverse
from conf.storage import OverwriteStorage
from django.utils.text import slugify
from utils.text import remove_accents

class Hero(models.Model):

    def upload_human_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(100000, 99999999)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(randomInt) + ext
        return "%s/%s" %("heroes", file_name)

    def upload_hero_3d_file_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(100000, 99999999)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(randomInt) + ext
        return "%s/%s" %("heroes_3d/", file_name)

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, default='', blank=True)
    description = models.CharField(max_length=1000, blank=True)
    thumbnail = models.FileField("Uploaded thumbnail of hero", storage=OverwriteStorage(), upload_to=upload_human_path, blank=True, null=True)
    price = models.BigIntegerField(default=0)

    # Basic abilities of hero
    physical_damage = models.IntegerField(default=0)
    magic_damage = models.IntegerField(default=0)
    physical_defence = models.IntegerField(default=0)
    magic_defence = models.IntegerField(default=0)
    attack_to_heal = models.IntegerField(default=0) # Per attack turn

    health = models.IntegerField(default=500)
    mana = models.IntegerField(default=400)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(remove_accents(self.name.lower()))
        super().save(*args, **kwargs)

from django.dispatch import receiver
@receiver(models.signals.pre_save, sender=Hero)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = Hero.objects.get(pk=instance.pk).thumbnail
        except Human.DoesNotExist:
            return
        else:
            new_avatar = instance.thumbnail
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)
