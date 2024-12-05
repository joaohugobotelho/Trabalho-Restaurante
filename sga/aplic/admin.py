from django.contrib import admin
from .models import Categoria, Prato, Pedido, ItemPedido, Bebida

# Inline para ItemPedido no admin
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

# Configuração para exibir os pedidos no admin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_cliente', 'usuario', 'data_pedido', 'total']
    inlines = [ItemPedidoInline]
    search_fields = ['nome_cliente', 'usuario__username']
    list_filter = ['data_pedido']

# Configuração para exibir os pratos no admin
@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria']
    search_fields = ['nome', 'categoria__nome']
    list_filter = ['categoria']

# Configuração para exibir as categorias no admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

# Configuração para exibir as bebidas no admin
@admin.register(Bebida)
class BebidaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']
