from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from aplic.views import (
    ListagemPratosView,
    adicionar_ao_carrinho,
    carrinho_view,
    remover_item_carrinho,
    ListagemBebidasView,  # Caso precise listar bebidas
    ListagemPedidosView,  # Caso precise listar pedidos
)

urlpatterns = [
    # Página inicial
    path('', views.IndexView.as_view(), name='index'),

    # Rotas de autenticação
    path('login/', views.custom_login, name='login'),  # Login personalizado
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout com redirecionamento para login
    path('register/', views.register, name='register'),  # Registro de usuários

    # Rotas de pratos
    path('pratos/', ListagemPratosView.as_view(), name='listagem_pratos'),  # Listagem de pratos
    path('detalhes_prato/<int:prato_id>/', views.detalhes_prato, name='detalhes_prato'),  # Detalhes de um prato específico

    # Carrinho
    path('carrinho/', carrinho_view, name='carrinho'),  # Página do carrinho
    path('adicionar_ao_carrinho/<int:prato_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),  # Adicionar ao carrinho
    path('remover_item/<int:item_id>/', remover_item_carrinho, name='remover_item'),  # Remover item do carrinho
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),  # Finalizar pedido
    path('sucesso_pedido/', views.sucesso_pedido, name='sucesso_pedido'),  # Sucesso do pedido

    # Rotas adicionais (caso necessário)
    path('bebidas/', ListagemBebidasView.as_view(), name='listagem_bebidas'),  # Listagem de bebidas
    path('pedidos/', ListagemPedidosView.as_view(), name='listagem_pedidos'),  # Listagem de pedidos
]

# Suporte para arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
