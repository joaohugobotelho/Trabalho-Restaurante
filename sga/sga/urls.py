from django.contrib import admin
from django.urls import path, include
from aplic import views  # Importa as views personalizadas de 'aplic'
from django.contrib.auth import views as auth_views  # Importa auth_views para autenticação
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel administrativo
    path('', views.custom_login, name='login'),  # Página inicial redireciona para login personalizado
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout com redirecionamento para login
    path('aplic/', include('aplic.urls')),  # Inclui rotas do aplicativo
]

# Suporte para arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
