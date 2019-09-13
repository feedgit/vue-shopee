from django.db import models
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from utils.text import remove_accents
from django.utils.text import slugify
import os, mimetypes, fnmatch, requests, random, json
from django.conf import settings
from django.http import JsonResponse

from django.core.files.base import ContentFile

def crawling_user_instagram(request):
    url = 'https://www.instagram.com/web/search/topsearch/'
    params = { "context": "blended", "query": "mia" }
    response = requests.get(url, params=params)
    for res in response.json().get('users'):
        user = res.get('user')
        if not User.objects.filter(username=user.get('username')).exists():
            phone_number = random.randint(10000000, 99999999)
            new_user = User.objects.create(name=user.get('full_name'), username=user.get('username'), email=user.get('username') + '@gmail.com', phone_number=phone_number)
            if user.get('profile_pic_url', None):
                image_content = ContentFile(requests.get(user.get('profile_pic_url')).content)
                new_user.avatar.save(user.get('username') + '.jpg', image_content)

    return JsonResponse({'msg': 'ok'}, status=200)
