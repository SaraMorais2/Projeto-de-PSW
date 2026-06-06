from django.urls import path
from . import views


app_name = 'cursos'

urlpatterns = [
    
    path('', views.listar_cursos, name='listar_cursos'),  
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),    
    path('editar/<int:id>/', views.atualizar_curso, name='atualizar_curso'),    
    path('deletar/<int:id>/', views.deletar_curso, name='deletar_curso'),
    path('<int:id>/', views.detail_curso, name='detail_curso'),
]