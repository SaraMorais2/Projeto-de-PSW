from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=230)
    matricula = models.CharField(max_length=8)  
    curso = models.CharField(max_length=230)  

    def __str__(self):
        return self.nome
