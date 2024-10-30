# meu_app/forms.py

from django import forms
from .models import Prato

class PratoForm(forms.ModelForm):
    remover_imagem = forms.BooleanField(required=False)

    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'imagem', 'remover_imagem']
