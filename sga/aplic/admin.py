from django.contrib import admin
from .models import Categoria, Prato, Cliente, Pedido, ItemPedido, Reserva

admin.site.register(Categoria)
admin.site.register(Prato)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Reserva)

