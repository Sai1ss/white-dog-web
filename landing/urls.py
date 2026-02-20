from django.urls import path
from . import views

# Estas son las rutas específicas de la aplicación "landing"
urlpatterns = [
    # Cuando alguien entre a la raíz de la app, muestra la vista "home"
    path('', views.home, name='home'),

    path('contacto/', views.contacto_view, name='contacto'), 
    path('gracias/', views.success_view, name='success'), # La necesitaremos para el paso siguiente
]