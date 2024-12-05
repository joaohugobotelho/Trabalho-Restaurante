from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Pedido, Bebida, Prato, Categoria, ItemPedido
from .forms import PedidoForm
from django.views.generic import CreateView
from django.contrib import messages
from .models import ItemCarrinho, Carrinho
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect("login")  
        else:
            messages.error(request, "Erro no cadastro. Verifique os campos preenchidos.")
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("home") 
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, "login.html")

# View personalizada para login
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html') 

@login_required
def detalhes_prato(request, prato_id):
    prato = get_object_or_404(Prato, id=prato_id)  
    return render(request, 'detalhes_prato.html', {'prato': prato})

@method_decorator(login_required, name='dispatch')
class PedidoPratoView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_prato.html'
    success_url = reverse_lazy('carrinho')

    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido.usuario = self.request.user
        pedido.save()
        return super().form_valid(form)
    
# Página inicial (após login)
@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'


# Listagem de pratos
@method_decorator(login_required, name='dispatch')
class ListagemPratosView(ListView):
    model = Prato
    template_name = 'listagem_pratos.html'
    context_object_name = 'pratos'

    def get_queryset(self):
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            return Prato.objects.filter(categoria_id=categoria_id)
        return Prato.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


# Adicionar ao carrinho
@login_required

def adicionar_ao_carrinho(request, prato_id):
    # Obtem o prato com base no ID ou retorna um erro 404
    prato = get_object_or_404(Prato, id=prato_id)

    # Obtém a quantidade do POST; padrão é 1
    quantidade = int(request.POST.get("quantidade", 1))

    # Obtém ou cria o carrinho do usuário
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    # Tenta obter ou criar o item do carrinho
    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        prato=prato,
        defaults={"quantidade": quantidade},  
    )

    if not criado:
        item.quantidade += quantidade
        item.save()

    messages.success(request, f"{prato.nome} adicionado ao carrinho com sucesso!")


    return redirect("carrinho")

#fun para alterar a quantidade de itens
def alterar_quantidade(request, item_id):
    if request.method == "POST":
        quantidade = int(request.POST.get("quantidade", 1))
        item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)

        if quantidade > 0:
            item.quantidade = quantidade
            item.save()
            messages.success(request, f"A quantidade do prato {item.prato.nome} foi atualizada para {quantidade}.")
        else:
            item.delete()
            messages.success(request, f"O prato {item.prato.nome} foi removido do carrinho.")

    return redirect("carrinho")


# Visualizar carrinho
@login_required
def carrinho_view(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    itens = carrinho.itens.all() 
    total = sum(item.subtotal() for item in itens)
    return render(request, "carrinho.html", {"itens": itens, "total": total})


# Remover item do carrinho
@login_required
def remover_item_carrinho(request, item_id):
    # Obtém o carrinho do usuário logado
    carrinho = get_object_or_404(Carrinho, usuario=request.user)

    # Obtém o item do carrinho que o usuário quer remover
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho=carrinho)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Item removido com sucesso!")
    
    return redirect("carrinho") 


# Finalizar pedido
@login_required
def finalizar_pedido(request):
    carrinho = get_object_or_404(Carrinho, usuario=request.user)

    # Verifica se o carrinho tem itens
    if not carrinho.itens.exists():
        messages.error(request, "Seu carrinho está vazio!")
        return redirect("carrinho")

    # Cria o pedido
    pedido = Pedido.objects.create(usuario=request.user, nome_cliente=request.user.username)

    # Transfere os itens do carrinho para o pedido
    for item_carrinho in carrinho.itens.all():
        ItemPedido.objects.create(
            pedido=pedido,
            prato=item_carrinho.prato,
            quantidade=item_carrinho.quantidade,
        )

    # Limpa o carrinho após transferir os itens
    carrinho.itens.all().delete()

    messages.success(request, "Pedido finalizado com sucesso!")
    return redirect("sucesso_pedido")  



# Mensagem de sucesso do pedido
@login_required
def sucesso_pedido(request):
    return render(request, 'sucesso_pedido.html')


# Listagem de bebidas
@method_decorator(login_required, name='dispatch')
class ListagemBebidasView(ListView):
    model = Bebida
    template_name = 'listagem_bebidas.html'
    context_object_name = 'bebidas'


# Listagem de pedidos
@method_decorator(login_required, name='dispatch')
class ListagemPedidosView(ListView):
    model = Pedido
    template_name = 'listagem_pedidos.html'
    context_object_name = 'pedidos'


def user_logout(request):
    if request.method == 'GET':  
        return redirect('login') 
    return redirect('listagem_pratos') 