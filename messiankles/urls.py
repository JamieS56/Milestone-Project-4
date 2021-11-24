from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('players/', include('players.urls')),
    path('teams/', include('teams.urls')),
    path('profile/', include('profiles.urls')),
    path('tickets/', include('tickets.urls')),
    path('fixtures/', include('fixtures.urls')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
