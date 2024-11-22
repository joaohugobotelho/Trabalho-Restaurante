from django.contrib import admin
from .models import Categoria, Prato,  Pedido, ItemPedido 

admin.site.register(Categoria)
admin.site.register(Prato)
#admin.site.register(Cliente)
#admin.site.register(Pedido)
admin.site.register(ItemPedido)

class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido
    extra = 1
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['prato','nome_cliente', 'quantidade', 'data_pedido']   
    inlines = [
        ItemPedidoInLine
    ]



 