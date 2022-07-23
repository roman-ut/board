from django.apps import AppConfig


class BoardappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boardApp'

    def ready(self):
        import boardApp.signals
