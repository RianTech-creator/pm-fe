from django.urls import path
from . import views
from usuario.views import home_view # Usando uma view existente como placeholder

# Estas são URLs provisórias para evitar o erro NoReverseMatch.
# Você deverá substituí-las pelas views corretas do app 'pedido' futuramente.
urlpatterns = [
    path('login/', views.usuario_login, name='usuario_login'),
    path('cadastro/', views.usuario_cadastrar, name='usuario_cadastrar'),
    path('painel/', views.usuario_painel, name='usuario_painel'), # Nova URL para o painel
    path('listar/', home_view, name='listar_pedidos'),
    path('criar/', home_view, name='criar_pedidos'),
    path('historico/', views.usuario_historico, name='usuario_historico'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('painel_cantineiro/', views.painel_cantineiro, name='painel_cantineiro'),
]