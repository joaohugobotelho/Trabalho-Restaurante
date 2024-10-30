from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Prato
from .forms import PratoForm
import logging

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CardapioView(TemplateView):
        template_name = 'cardapio.html'
        def get_context_data(self, **kwargs):
            context = super(CardapioView, self).get_context_data(**kwargs)
            return context



logger = logging.getLogger('django')

def adicionar_prato(request):
    if request.method == 'POST':
        logger.debug(f"Dados POST recebidos: {request.POST}")
        logger.debug(f"Arquivos recebidos: {request.FILES}")
        
        form = PratoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info("Prato adicionado com sucesso.")
            return redirect('lista_pratos')  # Redireciona para lista de pratos
        else:
            logger.warning("Formulário inválido.")
    else:
        form = PratoForm()
    
    return render(request, 'adicionar_prato.html', {'form': form})