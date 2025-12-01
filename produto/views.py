from django.shortcuts import render, redirect
from .models import Produto
from django.contrib import messages

# Create your views here.
def cadastrar_produto(request):
    """
    Cadastra um novo produto no banco de dados.
    - Se a requisição for GET, apenas renderiza o formulário.
    - Se a requisição for POST, processa os dados do formulário,
      cria um novo produto e o salva.
    """
    if request.method == 'POST':
        # Coleta os dados do formulário
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        categoria = request.POST.get('categoria')
        estoque = request.POST.get('estoque')
        foto = request.POST.get('foto')

        # Cria e salva o novo produto
        Produto.objects.create(nome=nome, preco=preco, categoria=categoria, estoque=estoque, foto=foto)
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('painel_cantineiro') # Redireciona para o painel após o cadastro

    return render(request, 'adicionar_estoque.html')

def listar_produtos(request):
    return render(request, 'listar_produto.html')

def editar_produto(request):
    return render(request, 'editar_produto.html')

def deletar_produto(request):
    return render(request, 'deletar_produto.html')

def adicionar_estoque(request):
    return render(request, 'adicionar_estoque.html')
