from django.urls import path
from django.conf.urls.static import static
#from .views import IndexView
#from .views import CardapioView
from .views import ListagemPratosView, DetalhesPratoView, PedidoPratoView
from django.conf import settings
from django.urls import path
from . import views
from aplic.views import ListagemPratosView





urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('cardapio/', views.CardapioView.as_view(), name='cardapio'), 
    path('pratos/', ListagemPratosView.as_view(), name='listagem_pratos'),
    path('pedido/', PedidoPratoView.as_view(), name='pedido_prato'),
    path('cardapio/', ListagemPratosView.as_view(), name='cardapio'),
    path('detalhes_prato/<str:nome>/', views.detalhes_prato, name='detalhes_prato'),
    path('sucesso_pedido/', views.sucesso_pedido, name='sucesso_pedido'),




    ]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
