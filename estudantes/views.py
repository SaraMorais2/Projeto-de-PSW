from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Alunos
from .forms import AlunoForm 

# 1. LISTA OS ALUNOS
def index(request):
    latest_alunos_list = Alunos.objects.order_by("nome")[:5]
    context = {"latest_alunos_list": latest_alunos_list}
    return render(request, "estudantes/index.html", context)

# 2. ADICIONAR NOVO ALUNO
def adicionar(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudantes:index')
    else:
        form = AlunoForm()
    return render(request, "estudantes/adicionar.html", {"form": form})

# 3. DETALHES DO ALUNO
def detail(request, aluno_id):
    aluno = get_object_or_404(Alunos, pk=aluno_id)
    return render(request, "estudantes/detail.html", {"aluno": aluno})

# 4. ATUALIZAR ALUNO
def atualizar_view(request, id):
    aluno = get_object_or_404(Alunos, pk=id)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('estudantes:index')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, "estudantes/adicionar.html", {"form": form, "aluno": aluno})

# 5. DELETAR ALUNO
def deletar_view(request, id):
    aluno = get_object_or_404(Alunos, pk=id)
    aluno.delete()
    return redirect('estudantes:index')