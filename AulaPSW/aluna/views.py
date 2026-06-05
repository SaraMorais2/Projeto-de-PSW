from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Essa é a rota de Teste!")

def adicionar_view(request, id):
    return HttpResponse(f"Adicionando o item com ID: {id}")

def deletar_view(request, id):
    return HttpResponse(f"Deletando o item com ID: {id}")

def atualizar_view(request):
    return HttpResponse("Atualize algo!")
