from rest_framework import serializers
from .models import Curso, Modulo, Inscricao

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao']

class ModuloSerializer(serializers.ModelSerializer):
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)

    class Meta:
        model = Modulo
        fields = ['id', 'nome', 'curso', 'curso_nome']

class InscricaoSerializer(serializers.ModelSerializer):
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)

    class Meta:
        model = Inscricao
        fields = ['id', 'curso', 'curso_nome', 'estudante']
