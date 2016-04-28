from django.apps import AppConfig

class RolesConfig(AppConfig):
    name = 'roles'
    verbose_name = "Roles"

    def ready(self):
        import roles.signals