from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from django.db import models
from apps.product.models import Product

class ReviewManager(models.Manager):
    def all(self):
        qs = super(ReviewManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, post):
        qs = super(ReviewManager, self).filter(post=post).filter(parent=None)
        return qs

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, related_name='replies', blank=True, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments')

    objects = ReviewManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.content)

    @property
    def children(self): #replies
        return Review.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
