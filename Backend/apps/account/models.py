from django.db import models
import time, os, shutil, random
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from conf.storage import OverwriteStorage

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")

        user = self.model(
             email = self.normalize_email(email),
             username = username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class User(AbstractUser):

    def upload_avatar_path(instance, filename):
        timestamp = int(time.time())
        randomInt = random.randint(0, 20)
        ext = os.path.splitext(filename)[1]
        file_name = str(timestamp) + '_' + str(random.randint(10000, 99999999)) + '_' + str(random.randint(10, 999)) + ext
        return "%s/%s" %("profiles", file_name)

    GENDER_CHOICES  =(('M', 'Male'), ('F', 'Female'))

    phone_number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.FileField("Uploaded avatar of profile", storage=OverwriteStorage(), upload_to=upload_avatar_path, blank=True, null=True)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    facebook_id = models.CharField(max_length=100, null=True, blank=True)
    google_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    coin = models.BigIntegerField(default=10)

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    @property
    def full_name(self):
        full_name = ''
        if self.first_name:
            full_name = self.first_name
        if self.last_name:
            full_name = full_name + ' ' + self.last_name
        return full_name
