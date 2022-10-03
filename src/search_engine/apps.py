from django.apps import AppConfig


class SearchEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_engine'
    verbose_name = 'Поисковое приложение (search engine)'
