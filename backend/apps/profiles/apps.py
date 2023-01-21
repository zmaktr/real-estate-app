from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.profiles"

    #overriding the AppConfig ready() method to configure signals
    def ready(self):
        from apps.profiles import signals
