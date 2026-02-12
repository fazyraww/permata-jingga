from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as token_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Konfigurasi Swagger disamakan dengan gaya temanmu
schema_view = get_schema_view(
   openapi.Info(title="Travel API", default_version='v1'),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Menghubungkan ke aplikasi kamu (pemesanan)
    path('', include('pemesanan.urls')),
    
    # Login via Token (Sama persis dengan api-token-auth temanmu)
    path('api-token-auth/', token_views.obtain_auth_token),
    
    # Auth bawaan Django untuk session login/logout
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Dokumentasi API (Docs)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]