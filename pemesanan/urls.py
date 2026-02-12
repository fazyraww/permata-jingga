from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Library JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Router untuk API
router = DefaultRouter()
router.register(r'kelas-travel', views.KelasTravelViewSet)
router.register(r'jadwal', views.JadwalViewSet)
router.register(r'tiket', views.TiketViewSet)
router.register(r'operasional', views.BiayaOperasionalViewSet)

urlpatterns = [
    # 1. API AUTH (Prioritas Utama untuk Login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 2. API DATA (Endpoints JSON)
    path('api/', include(router.urls)),
    
    # 3. WEB VIEWS (Render HTML Templates)
    path('', views.web_login, name='home'),
    path('login-frontend/', views.web_login, name='login-frontend'),
    path('dashboard/', views.web_tiket_list, name='dashboard'),
    path('tiket-list/', views.web_tiket_list, name='tiket-list'),
    path('jadwal-armada/', views.web_jadwal_armada, name='jadwal-armada'),
    path('sopir/', views.web_sopir_list, name='sopir-list'),
    
    # 4. CRUD TIKET (Django Class Based Views)
    path('tiket/baru/', views.TiketCreateView.as_view(), name='tiket-create'),
    path('tiket/<int:pk>/edit/', views.TiketUpdateView.as_view(), name='tiket-update'),
    path('tiket/<int:pk>/hapus/', views.TiketDeleteView.as_view(), name='tiket-delete'),
]