# core/views.py

from django.shortcuts import render
from rest_framework import viewsets
from .models import Curso, Modulo, Inscricao
from .serializers import CursoSerializer, ModuloSerializer, InscricaoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

# NOVA VIEW PARA FRONTEND
def index(request):
    return render(request, 'index.html')
