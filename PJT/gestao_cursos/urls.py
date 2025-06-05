from django.contrib import admin
from django.urls import path, include
from core.views import index
from rest_framework import routers
from core.views import CursoViewSet, ModuloViewSet, InscricaoViewSet

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'modulos', ModuloViewSet)
router.register(r'inscricoes', InscricaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', index),  # SPA entry point
]
