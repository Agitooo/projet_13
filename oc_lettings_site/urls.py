from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.home.urls')),
    path('lettings/', include('apps.lettings.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('admin/', admin.site.urls),
]
