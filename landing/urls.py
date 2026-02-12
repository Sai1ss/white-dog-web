from django.urls import path
from . import views

# Estas son las rutas específicas de la aplicación "landing"
urlpatterns = [
    # Cuando alguien entre a la raíz de la app, muestra la vista "home"
    path('', views.home, name='home'),
]