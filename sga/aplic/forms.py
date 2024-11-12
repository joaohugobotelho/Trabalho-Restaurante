# meu_app/forms.py

from django import forms
from .models import Prato
from .models import Usuario

class PratoForm(forms.ModelForm):
    remover_imagem = forms.BooleanField(required=False)

    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'imagem', 'remover_imagem']

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']