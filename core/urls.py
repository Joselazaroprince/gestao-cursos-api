from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, ModuloViewSet, InscricaoViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'modulos', ModuloViewSet)
router.register(r'inscricoes', InscricaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
