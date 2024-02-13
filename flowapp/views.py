from django.shortcuts import render
from .models import Aluno

def cadastro(request):
    return render(request, 'cadastro.html')

def alunos(request):
    aluno_cadastro = Aluno()
    aluno_cadastro.nome = request.POST.get('nome')
    aluno_cadastro.faixa = request.POST.get('faixa')
    aluno_cadastro.data = request.POST.get('data')
    aluno_cadastro.save()

    return render(request,'cadastrado.html')
    