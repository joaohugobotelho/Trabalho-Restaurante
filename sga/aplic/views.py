from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Prato
from .forms import PratoForm
from django.views import View
from django.shortcuts import render
from .forms import UsuarioForm



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

def adicionar_prato(request):
    if request.method == 'POST':
        form = PratoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pratos')
    else:
        form = PratoForm()
    return render(request, 'adicionar_prato.html', {'form': form})


class BebidasView(View):
    def get(self, request):
        return render(request, 'bebidas.html')

    
class EntradasView(View):
    def get(self, request):
        return render(request, 'entradas.html')
    
class PratosView(View):
    def get(self, request):
        return render (request, 'pratos.html') 

    
class SobreView(View):
    def get(self, request):
        return render(request, 'sobre.html')

class DeliveryView(View):
    def get(self, request):
        return render(request, 'delivery.html')

class ReservaView(View):
    def get(self, request):
        return render(request, 'reserva.html')
    
class SobremesaView(View):
    def get(self, request):
        return render(request, 'sobremesas.html')
    
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso') 
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})

   





