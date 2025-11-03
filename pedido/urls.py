from django.urls import path
from . import views

urlpatterns = [
    path('criar_pedido/', views.criar_pedidos, name='criar_pedido'),
    path('historico/', views.historico, name='historico_pedidos'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
    path('carrinho/', views.carrinho, name='carrinho'),
]