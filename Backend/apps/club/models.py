import time, random, os
from django.db import models
from django.urls import reverse
from conf.storage import OverwriteStorage
from django.utils.text import slugify
from utils.text import remove_accents

class Club(models.Model):

    def upload_clubs_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(100000, 99999999)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(randomInt) + ext
        return "%s/%s" %("clubs", file_name)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, default='')
    description = models.CharField(max_length=1000, blank=True)
    thumbnail = models.FileField("Uploaded thumbnail of club", storage=OverwriteStorage(), upload_to=upload_clubs_path, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(remove_accents(self.name.lower()))
        super().save(*args, **kwargs)
