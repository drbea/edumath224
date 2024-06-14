"""config URL Configuration"""
from django.contrib import admin
from django.urls import include, path

# from config import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('auth/', include('authentification.urls')),
    path('api/', include('api.urls')),
]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
