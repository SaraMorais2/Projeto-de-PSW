from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm  # 👈 Importamos o novo form

# LER (Listagem)
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

# CRIAR (Adicionar)
def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva direto no banco de dados!
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'cursos/form_curso.html', {'form': form})

# ATUALIZAR (Editar)
def atualizar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso) # Vincula o form ao curso existente
        if form.is_valid():
            form.save()
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm(instance=curso) # Carrega os dados atuais do curso nos campos
    
    return render(request, 'cursos/form_curso.html', {'form': form, 'curso': curso})

# DELETAR (Excluir)
def deletar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST' or request.GET.get('confirm') == 'yes':
        curso.delete()
    return redirect('cursos:listar_cursos')