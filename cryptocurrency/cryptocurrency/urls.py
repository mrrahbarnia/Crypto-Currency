"""
URL's for entire project.
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bitcoin/', include('bitcoin.urls')),
    path('bitcoin/api/', include('bitcoin.api.urls')),
    # ========== Rest api documentation for development ==========
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    # urlpatterns += static(
    #     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    # )
