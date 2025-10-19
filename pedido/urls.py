from django.urls import path
from . import views

urlpatterns = [
    path('criar_pedido/', views.criar_pedidos, name='criar_pedido'),
    path('historico_pedidos/', views.historico_pedidos, name='historico_pedidos'),
    path('listar/', views.listar_pedidos, name='listar_pedidos'),
]