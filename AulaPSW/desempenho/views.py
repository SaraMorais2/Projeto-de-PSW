from django.shortcuts import render, redirect, get_object_or_404
from .models import Notas
from .forms import NotasForm


def notas(request):
    notas = Notas.objects.all().select_related('aluno') # Otimiza a busca trazendo o aluno junto
    return render(request, 'desempenho/notas.html', {'notas': notas})

# LANÇAR NOTA
def adicionar_nota(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desempenho:notas')
    else:
        form = NotasForm()
    return render(request, 'desempenho/forms_notas.html', {'form': form})

# EDITAR NOTA
def atualizar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    if request.method == 'POST':
        form = NotasForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('desempenho:notas')
    else:
        form = NotasForm(instance=nota)
    return render(request, 'desempenho/forms_notas.html', {'form': form, 'nota': nota})

# EXCLUIR NOTA
def deletar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    if request.method == 'POST' or request.GET.get('confirm') == 'yes':
        nota.delete()
    return redirect('desempenho:notas')