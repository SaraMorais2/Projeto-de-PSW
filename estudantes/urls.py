from django.urls import path
from . import views  

app_name = "estudantes"

urlpatterns = [
    # Lista de Alunos
    path("", views.index, name="index"), 
    
    # Perfil do Aluno
    path("<int:aluno_id>/", views.detail, name="detail"),
    
    # Formulário de Cadastro
    path("adicionar/", views.adicionar, name="adicionar"),
    
    # Rota de Edição (Usa 'id' para bater com sua atualizar_view)
    path('atualizar/<int:id>/', views.atualizar_view, name='atualizar'),
    
    # Rota de Exclusão (Usa 'id' para bater com sua deletar_view)
    path('deletar/<int:id>/', views.deletar_view, name='deletar'),
]