import time, random, os
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.urls import reverse
from conf.storage import OverwriteStorage
from django.utils.text import slugify
from utils.text import remove_accents

# What features make product different?
class ProductFeature(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, default='')
    is_suggested = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(remove_accents(self.name.lower()))
        super().save(*args, **kwargs)

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, default='')
    parent = models.ForeignKey('self', null=True, related_name='children_categories', blank=True, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    is_suggested = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(remove_accents(self.name.lower()))
        super().save(*args, **kwargs)

class Product(models.Model):

    def upload_product_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(100000, 99999999)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(randomInt) + ext
        return "%s/%s" %("products", file_name)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, default='')
    description = models.CharField(max_length=1000, blank=True)
    thumbnail = models.FileField("Uploaded thumbnail of product", storage=OverwriteStorage(), upload_to=upload_product_path, blank=True, null=True)

    categories = models.ManyToManyField(ProductCategory, blank=True)
    features = models.ManyToManyField(ProductFeature, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("products:view", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(remove_accents(self.name.lower()))
        super().save(*args, **kwargs)
