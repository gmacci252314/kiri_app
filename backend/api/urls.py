from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraducaoViewSet

router = DefaultRouter()
router.register(r'traducoes', TraducaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]