from django.urls import path
from django.conf.urls.static import static
from .views import IndexView
from .views import CardapioView
from .views import BebidasView
from .views import PratosView
from .views import EntradasView
from .views import SobreView
from django.conf import settings
from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cardapio/', views.CardapioView.as_view(), name='cardapio'), 
    path('pratos/', views.PratosView.as_view(), name='pratos'), 
    path('entradas/', views.EntradasView.as_view(), name='entradas'),
    path('sobre/', views.SobreView.as_view(), name='sobre'), 
    path('bebidas/', views.BebidasView.as_view(), name='bebidas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
