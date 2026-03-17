from django.contrib import admin
from django.urls import path, include
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí delegamos todo el tráfico de la portada a la app 'landing'
    path('', include('landing.urls')), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)