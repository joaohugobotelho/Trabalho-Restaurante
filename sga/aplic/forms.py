from django import forms
from .models import Prato, Pedido

class PratoForm(forms.ModelForm):
    remover_imagem = forms.BooleanField(required=False)

    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'imagem']  # 'remover_imagem' não faz parte do modelo, foi removido


class UsuarioForm(forms.Form):  # Alterado para usar `forms.Form` já que não há um modelo associado
    nome = forms.CharField(max_length=255)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente']  # Ajustado para refletir os campos reais do modelo Pedido
