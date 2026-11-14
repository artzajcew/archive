from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("archive.urls")),
]

handler404 = "archive.views.custom_404"

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
