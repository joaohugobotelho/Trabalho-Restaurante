from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import PratoForm
from django.views import View
from django.shortcuts import render
#from .forms import UsuarioForm
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from .models import Prato, Pedido, Bebida
from django import forms
from .forms import PedidoForm


def adicionar_prato(request):
    if request.method == 'POST':
        form = PratoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pratos')
    else:
        form = PratoForm()
    return render(request, 'adicionar_prato.html', {'form': form})


class ListagemPratosView(ListView):
    model = Prato
    template_name = 'listagem_pratos.html'
    context_object_name = 'pratos'

class DetalhesPratoView(View):
    def get(self, request, id):
        prato = Prato.objects.get(id=id) 
        return render(request, 'detalhes_prato.html', {'prato': prato})

class PedidoPratoView(View):
    def get(self, request):
        pratos = Prato.objects.all() 
        bebidas = Bebida.objects.all() 
        return render(request, 'pedido_prato.html', {'pratos': pratos, 'bebidas': bebidas})


    def form_valid(self, form):
        return super().form_valid(form)

class PedidoView(View):
    def get(self, request):
        pedidos = Pedido.objects.all()  

        return render(request, 'pedido.html', {'pedidos': pedidos})


class IndexView(TemplateView):
    template_name = 'index.html'
    def index(request):
        pratos = Prato.objects.all()  
        return render(request, 'index.html', {'pratos': pratos})

def criar_pedido(request):
    if request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente', 'Anônimo') 
        
        prato_id = request.POST.get('prato_id')
        quantidade = request.POST.get('quantidade')

        
        prato = Prato.objects.get(id=prato_id)
        
        pedido = Pedido(nome_cliente=nome_cliente, prato=prato, quantidade=quantidade)
        
        pedido.save()
        
        return redirect('pedido_sucesso')  
    else:
        pratos = Prato.objects.all()
        return render(request, 'pedido_prato.html', {'pratos': pratos})

def detalhes_prato(request, nome):
    prato = Prato.objects.get(nome=nome) 
    return render(request, 'detalhes_prato.html', {'prato': prato})

def pedido_prato(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('sucesso_pedido')  
    else:  
        form = PedidoForm()

    return render(request, 'pedido_prato.html', {'form': form})

def sucesso_pedido(request):
    return render(request, 'sucesso_pedido.html')
