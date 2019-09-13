from  django.core.exceptions import ValidationError
from django.db.models import signals
from .models import *
from apps.account.models import User

def validate_enough_coin_before_buying_hero(sender, instance, **kwargs):
    if instance.user.coin < instance.hero.price:
        raise ValidationError({'gold': 'Sorry you do not have enough gold to charge this'})

def validate_enough_coin_before_buying_equipment(sender, instance, **kwargs):
    if instance.user.coin < instance.equipment.price:
        raise ValidationError({'gold': 'Sorry you do not have enough gold to charge this'})

def charge_coin_after_buying_equipment(sender, instance, **kwargs):
    instance.user.coin - instance.equipment.price

def charge_coin_after_buying_hero(sender, instance, **kwargs):
    instance.user.coin - instance.hero.price

signals.pre_save.connect(validate_enough_coin_before_buying_equipment, sender=UserEquipment)
signals.post_save.connect(charge_coin_after_buying_equipment, sender=UserEquipment)

signals.pre_save.connect(validate_enough_coin_before_buying_hero, sender=UserHero)
signals.post_save.connect(charge_coin_after_buying_hero, sender=UserHero)
