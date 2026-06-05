from django import forms
from .models import Notas

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['aluno', 'disciplina', 'valor']
        
        widgets = {
            'aluno': forms.Select(attrs={
                'class': 'form-select'
            }),
            'disciplina': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Matemática, Estrutura de Dados'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'min': '0',
                'max': '10',
                'placeholder': '0.00'
            }),
        }

        labels = {
            'aluno': 'Selecione o Aluno',
            'disciplina': 'Nome da Disciplina',
            'valor': 'Nota (0 a 10)',
        }