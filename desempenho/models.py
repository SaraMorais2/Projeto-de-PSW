from django.db import models
from estudantes.models import Alunos # Importa o aluno do outro app

class Notas(models.Model):
    aluno = models.ForeignKey(
        Alunos, 
        on_delete=models.CASCADE,
        related_name='notas' # Esse nome agora é único no projeto!
    )
    disciplina = models.CharField(max_length=230)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.disciplina}: {self.valor} ({self.aluno.nome})"