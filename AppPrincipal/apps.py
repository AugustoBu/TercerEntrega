from django.apps import AppConfig

class AppPrincipalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppPrincipal'

    def ready(self):
        from .models import Categoria
        if Categoria.objects.count() == 0:
            Categoria.objects.create(nombre="Instrumentos")
            Categoria.objects.create(nombre="Accesorios")