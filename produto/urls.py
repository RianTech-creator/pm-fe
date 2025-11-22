from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('remover/<int:produto_id>/', views.remover_estoque, name='remover_estoque'),
]