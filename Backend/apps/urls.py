from rest_framework import routers
from django.urls import path, include
from conf import settings
from apps.account import views as user_views
from apps.equipment import views as equipment_views
from apps.hero import views as hero_views
from apps import views as global_views
from apps.authentication import custom_jwt
from apps.authentication import views as authentication_views
from apps.account_item import views as account_item_views
from rest_framework_jwt import views as rest_framework_jwt_views
from apps import crawl as crawl_views

router = routers.DefaultRouter()
router.register(r'user', user_views.UserViewSet, base_name='user')
router.register(r'equipment', equipment_views.EquipmentViewSet, base_name='equipment')
router.register(r'hero', hero_views.HeroViewSet, base_name='hero')

urlpatterns = [
    path('user/account/', user_views.get_user_account_information, name='get_user_account_information'),
    path('home_json/', global_views.get_homepage_data, name='get_homepage_data'),
    path('my-heroes/', account_item_views.get_my_heroes, name='get_my_heroes'),
    path('buy-hero/', account_item_views.buy_hero, name='buy_hero'),
    path('buy-equipment/', account_item_views.buy_equipment, name='buy_equipment'),
    path('my-equipments/', account_item_views.get_my_equipments, name='get_my_equipments'),
    path('register/', authentication_views.register, name='register'),
    path('auth/login/', rest_framework_jwt_views.obtain_jwt_token),
    path('auth/refresh-token/', rest_framework_jwt_views.refresh_jwt_token),
    path('auth/verify-token/', rest_framework_jwt_views.verify_jwt_token),
    path('crawl_data/', crawl_views.crawling_user_instagram, name='crawl_views'),
]
urlpatterns += router.urls
