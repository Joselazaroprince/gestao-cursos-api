from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Curso, Modulo, Inscricao
from .serializers import CursoSerializer, ModuloSerializer, InscricaoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome']

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'curso__nome']
    ordering_fields = ['nome']

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['estudante', 'curso__nome']
    ordering_fields = ['estudante']

def index(request):
    return render(request, 'index.html')