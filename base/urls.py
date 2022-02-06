from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from base import settings
from base.settings import API_PREFIX

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path(f'{API_PREFIX}/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]