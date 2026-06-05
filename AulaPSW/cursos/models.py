from django.db import models

class Curso(models.Model):
    
    OPCOES_TURNO = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
    ]

    nome = models.CharField(max_length=230)
    codigo = models.CharField(max_length=20, unique=True)
    carga_horaria = models.IntegerField(default=120)
    
    
    turno = models.CharField(
        max_length=20, 
        choices=OPCOES_TURNO, 
        default='Noturno'
    )

    def __str__(self):
        return f"{self.nome} ({self.turno})"