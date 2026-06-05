from django.db import models
from cursos.models import Curso 

class Alunos(models.Model):
    nome = models.CharField(max_length=230)
    matricula = models.CharField(max_length=8)  
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='alunos'
    )  

    def __str__(self):
        return self.nome