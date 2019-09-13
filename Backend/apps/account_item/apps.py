from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AccountItemConfig(AppConfig):
    name = 'apps.account_item'
    verbose_name = _('account_item')

    def ready(self):
        import apps.account_item.signals
