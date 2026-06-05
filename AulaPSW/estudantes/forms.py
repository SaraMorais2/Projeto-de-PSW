from django import forms
from .models import Alunos

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'matricula', 'curso']
