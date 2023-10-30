from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', include('apps.home.urls')),
    path('lettings/', include('apps.lettings.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    # Correction accessibilité static
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
