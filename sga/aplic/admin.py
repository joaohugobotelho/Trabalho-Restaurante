from django.contrib import admin
from .models import Categoria, Prato, Cliente, Pedido, ItemPedido, Reserva

admin.site.register(Categoria)
admin.site.register(Prato)
admin.site.register(Cliente)
#admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Reserva)

class ItemPedidoInLine(admin.TabularInline):
    model = ItemPedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente','data_pedido','total')
    inlines = [
        ItemPedidoInLine
    ]