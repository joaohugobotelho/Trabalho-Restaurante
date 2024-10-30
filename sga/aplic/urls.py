from django.urls import path
from django.conf.urls.static import static
from .views import IndexView
from .views import CardapioView
from django.conf import settings
from django.urls import path
from . import views
from .views import adicionar_prato


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cardapio', CardapioView.as_view(), name='cardapio'), 
<<<<<<< HEAD
    path('pratos/bolinho-bacalhau.jpg', views.adicionar_prato, name='adicionar_prato'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]


>>>>>>> 8b81e8941843884b6d6d2d4fbfcf1e7bdd2b40a5
