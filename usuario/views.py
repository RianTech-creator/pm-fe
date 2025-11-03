from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS
from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def logout_usuario(request):
    """
    Encerra a sessão do usuário.
    """
    logout(request)
    return redirect('home')

@csrf_exempt  # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS
def usuario_login(request):
    if request.method == 'POST':
         if request.method == 'POST':
            user = User()
            user.username = 'teste'
            user.email = 'user@email.com'
            user.set_password('senha123')

            usuario = Usuario()
            usuario.user = user
            usuario.role = 'cantineiro'
            usuario.username = 'Nome do Usuario'
            return render(request, 'usuario_painel.html', {'usuario': usuario})
    return render(request, 'usuario_login.html')

def usuario_cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Aqui você pode adicionar lógica para salvar o usuário no banco de dados
        # Por simplicidade, estamos apenas redirecionando para a página de login
        return redirect('usuario_login')
    return render(request, 'usuario_cadastrar.html')

def usuario_historico(request):
    return render(request, 'usuario_historico.html')

def painel_cantineiro(request):
    if request.method == 'POST':
         if request.method == 'POST':
            user = User()
            user.username = 'teste'
            user.email = 'user@email.com'
            user.set_password('senha123')

            usuario = Usuario()
            usuario.user = user
            usuario.role = 'cantineiro'
            usuario.username = 'Nome do Usuario'
            return render(request, 'painel_cantineiro.html', {'usuario': usuario})
    return render(request, 'usuario_login.html')

def usuario_painel(request):
    return render(request, 'usuario_painel.html')

def painel_cantineiro(request):
    return render(request, 'painel_cantineiro.html')


