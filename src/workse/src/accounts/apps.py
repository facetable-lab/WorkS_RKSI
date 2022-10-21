from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # Отображение в админке.
    verbose_name = 'Подписчики (accounts)'
