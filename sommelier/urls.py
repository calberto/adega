from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import core.urls

import core.urls

urlpatterns = [
    path('' , include('website.urls')),
    path('sistema/', include(core.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

