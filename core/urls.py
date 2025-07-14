# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, TenantProfileViewSet, AgreementViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'tenant-profiles', TenantProfileViewSet)
router.register(r'agreements', AgreementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
