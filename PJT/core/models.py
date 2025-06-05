from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Modulo(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscricoes')
    estudante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.estudante} - {self.curso.nome}"
