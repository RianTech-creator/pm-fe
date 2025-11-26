from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from produto.models import Produto

# Dados fictícios para o cardápio, já que ainda não há um modelo para ele.
# Isso deve ser substituído por uma consulta a um modelo 'Produto' ou 'ItemCardapio'.
DUMMY_CARDAPIO = [
    {'id': 1, 'nome': 'Misto Quente', 'descricao': 'Pão de forma, queijo e presunto.', 'preco': 5.50, 'imagem': 'images/misto_quente.jpeg'},
    {'id': 2, 'nome': 'Pão de Queijo', 'descricao': 'Unidade.', 'preco': 3.00, 'imagem': 'images/pao_de_queijo.jpeg'},
    {'id': 3, 'nome': 'Coxinha de Frango', 'descricao': 'Salgado frito recheado com frango.', 'preco': 6.00, 'imagem': 'images/coxinha.jpeg'},
    {'id': 4, 'nome': 'Suco de Laranja Natural', 'descricao': 'Copo de 300ml.', 'preco': 7.00, 'imagem': 'images/suco_laranja.jpeg'},
    {'id': 5, 'nome': 'Refrigerante Lata', 'descricao': 'Coca-cola, Guaraná ou Soda.', 'preco': 5.00, 'imagem': 'images/refrigerante.jpeg'},
]

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='usuario_login')
def listar_pedidos(request):
    return render(request, 'listar_pedidos.html')

# @login_required(login_url='usuario_login')
def criar_pedidos(request):
    """
    Exibe o cardápio para o usuário fazer um novo pedido (GET)
    e processa o pedido enviado (POST).
    """
    # cardapio = Produto.objects.all()
    cardapio = DUMMY_CARDAPIO
    if request.method == 'POST':
        # Lógica para processar o pedido.
        # Aqui você pegaria os itens do request.POST,
        # calcularia o total e criaria um objeto Pedido no banco.
        print("Dados do pedido recebido:", request.POST)
        # Após salvar o pedido, redireciona para o histórico ou uma página de confirmação.
        return redirect('historico_pedidos')

    context = {'cardapio': cardapio}
    return render(request, 'criar_pedido.html', context)

@login_required(login_url='usuario_login') #tirar login_required para verificar rota pedido/historico
def historico(request):
    return render(request, 'historico_pedidos.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def listar_pedidos(request):
    return render(request, 'listar_pedidos.html')

def status_pedido(request):
    return render(request, 'status_pedido.html')

def forma_pagamento(request):
    return render(request, 'pagamento.html')

def pagamento_feito(request):
    return render(request, 'pagamento_concluido.html')