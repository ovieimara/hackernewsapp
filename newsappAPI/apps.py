from django.apps import AppConfig

class NewsappapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsappAPI'

    def ready(self):
        from . import scheduler
        scheduler.start()
