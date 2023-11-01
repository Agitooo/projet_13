from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.views.defaults import page_not_found, server_error


urlpatterns = [
    path('', include('apps.home.urls')),
    path('lettings/', include('apps.lettings.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('admin/', admin.site.urls),
    # Correction accessibilité static
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^404/$', page_not_found),
    url(r'^500/$', server_error),
]
