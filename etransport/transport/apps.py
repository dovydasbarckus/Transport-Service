from django.apps import AppConfig


class TransportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transport'

    def ready(self):
        from .signals import create_profile, save_profile