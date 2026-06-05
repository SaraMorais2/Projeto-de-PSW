from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'codigo', 'carga_horaria', 'turno']
        
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Análise e Desenvolvimento de Sistemas'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: ADS-2026'
            }),
            'carga_horaria': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'turno': forms.Select(attrs={
                'class': 'form-select'
            }),
            }

        labels = {
            'nome': 'Nome do Curso',
            'codigo': 'Código Identificador',
            'carga_horaria': 'Carga Horária (Horas)',
            'turno': 'Turno',
        }