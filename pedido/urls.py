from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.criar_pedidos, name='criar_pedido'),
    path('historico/', views.historico, name='historico_pedidos'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('status/ <int:pedido_id>/', views.status_pedido, name='status_pedido'),
    path('carrinho/adicionar/ <int:produto_id>/', views.carrinho, name='adicionar_ao_carrinho'), 
    path('forma_pagamento/', views.forma_pagamento, name='forma_pagamento'),
    path('pagamento_concluido/', views.pagamento_feito, name='pagamento_feito'),
]