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
    ListagemBebidasView,  
    ListagemPedidosView,  
)

urlpatterns = [
    # Página inicial
    path('', views.IndexView.as_view(), name='index'),

    # Rotas de autenticação
    path('login/', views.custom_login, name='login'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
    path('register/', views.register, name='register'),  

    # Rotas de pratos
    path('pratos/', ListagemPratosView.as_view(), name='listagem_pratos'),  
    path('detalhes_prato/<int:prato_id>/', views.detalhes_prato, name='detalhes_prato'),  

    # Carrinho
    path('carrinho/', carrinho_view, name='carrinho'),  # Página do carrinho
    path('adicionar_ao_carrinho/<int:prato_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),  
    path('remover_item/<int:item_id>/', remover_item_carrinho, name='remover_item'),  
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),  
    path('sucesso_pedido/', views.sucesso_pedido, name='sucesso_pedido'),  

    # Rotas adicionais (caso necessário)
    path('bebidas/', ListagemBebidasView.as_view(), name='listagem_bebidas'),  
    path('pedidos/', ListagemPedidosView.as_view(), name='listagem_pedidos'),  
    path('logout/', views.user_logout, name='logout'),
    path('carrinho/alterar/<int:item_id>/', views.alterar_quantidade, name='alterar_quantidade'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
