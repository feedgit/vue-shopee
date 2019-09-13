from django.contrib import admin
from .models import *

admin.site.register(User)
from django.contrib.auth.models import Group

admin.site.unregister(Group)
