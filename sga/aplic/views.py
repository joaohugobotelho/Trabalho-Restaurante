from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Prato

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CardapioView(TemplateView):
        template_name = 'cardapio.html'
        def get_context_data(self, **kwargs):
            context = super(CardapioView, self).get_context_data(**kwargs)
            return context
