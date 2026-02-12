from django.contrib import admin
from django.urls import path, include  # <--- Importante: 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí delegamos todo el tráfico de la portada a la app 'landing'
    path('', include('landing.urls')), 
]