from django.db import models
from django.shortcuts import render
from django.utils import timezone




class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='media/',blank=True, null=True)


    def __str__(self):
        return self.nome



class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_pedido = models.DateTimeField(default=timezone.now)
    @property
    def total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"Pedido de {self.nome_cliente} - {self.prato.nome}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.prato.nome} (Pedido #{self.pedido.id})"

class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2) 
    descricao = models.TextField(blank=True, null=True)  
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)  


    def __str__(self):
        return self.nome








