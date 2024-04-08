from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar as dados da tela paar o banco d dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir todos os usuarios cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    #retornar os dados para a pagina de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)