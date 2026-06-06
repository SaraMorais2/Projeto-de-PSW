from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm  


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

def detail_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    alunos_do_curso = curso.alunos.all()
    return render(request, 'cursos/detail.html', {'curso': curso, 'alunos': alunos_do_curso})

def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'cursos/form_curso.html', {'form': form})
    


def atualizar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso) 
        if form.is_valid():
            form.save()
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm(instance=curso)    
    return render(request, 'cursos/form_curso.html', {'form': form, 'curso': curso})


def deletar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST' or request.GET.get('confirm') == 'yes':
        curso.delete()
    return redirect('cursos:listar_cursos')