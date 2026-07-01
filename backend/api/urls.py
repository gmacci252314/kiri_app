from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import traducao_list , TraducaoViewSet


router = DefaultRouter()
router.register(r'traducoes', TraducaoViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path("lista/", traducao_list, name="traducao_list"),
    path("cadastrar/", views.cadastrar_traducao, name="cadastrar"),
    path('editar/<int:id>/', views.editar_traducao, name='editar'),
    path('deletar/<int:id>/', views.deletar_traducao, name='deletar'),
    path('', views.home, name="home"),

]