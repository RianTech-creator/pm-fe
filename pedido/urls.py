from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.criar_pedidos, name='criar_pedido'),
    path('historico/', views.historico, name='historico_pedidos'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('status/', views.status_pedido, name='status_pedido'),
    path('carrinho/adicionar/ <int:produto_id/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'), 
]