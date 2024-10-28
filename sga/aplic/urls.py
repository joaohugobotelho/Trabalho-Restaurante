from django.urls import path
from .views import IndexView
from .views import CardapioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cardapio', CardapioView.as_view(), name='cardapio'), 
]