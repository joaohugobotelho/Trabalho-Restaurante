from django.db import models
from django.contrib.auth.models import User


# Modelo para Categorias de Pratos
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


# Modelo para Pratos
class Prato(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="media/", blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="pratos"
    )

    class Meta:
        verbose_name = "Prato"
        verbose_name_plural = "Pratos"

    def __str__(self):
        return self.nome


# Modelo para Pedidos
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    data_pedido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def total(self):
        # Calcula o total do pedido somando o subtotal de cada item
        return sum(item.subtotal() for item in self.itens.all())

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome_cliente}"


# Modelo para Itens de Pedido
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    def subtotal(self):
        # Calcula o subtotal com base na quantidade e no preço do prato
        return self.quantidade * self.prato.preco

    def __str__(self):
        return f"{self.quantidade}x {self.prato.nome} (Pedido #{self.pedido.id})"


# Modelo para Carrinho
class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"


# Modelo para Itens no Carrinho
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens")
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)  # Valor padrão de 1

    class Meta:
        verbose_name = "Item do Carrinho"
        verbose_name_plural = "Itens do Carrinho"

    def subtotal(self):
        return self.quantidade * self.prato.preco

    def __str__(self):
        return f"{self.quantidade} x {self.prato.nome} no {self.carrinho}"


# Modelo para Bebidas
class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

    def __str__(self):
        return self.nome
