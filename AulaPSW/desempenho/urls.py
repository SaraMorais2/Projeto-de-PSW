from django.urls import path
from . import views

app_name = 'desempenho'

urlpatterns = [
    path('', views.notas, name='notas'),
    path('lancar/', views.adicionar_nota, name='adicionar_nota'),
    path('editar/<int:id>/', views.atualizar_nota, name='atualizar_nota'),
    path('deletar/<int:id>/', views.deletar_nota, name='deletar_nota'),
]