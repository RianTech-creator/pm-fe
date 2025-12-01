from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produto'),
    path('editar/', views.editar_produto, name='editar_produto'),
    path('deletar/', views.deletar_produto, name='deletar_produto'),
    path('adicionar/', views.adicionar_estoque, name='adicionar_estoque'),
]