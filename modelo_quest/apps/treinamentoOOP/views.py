# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from modelo_quest.apps.treinamentoOOP.models import *
from django.views.generic import View #Importar para usar class-based-views (CBV)
from vanilla import CreateView, DeleteView, ListView, UpdateView, TemplateView


# Exemplo 2 (CBV)
class CadastrarCBV(View):
    """docstring for Cadastrar CBV"""
    tipoForm = None
    sucesso = False

    def get(self, request):
        cadastroForm = self.tipoForm()
        return render(request, 'cadastro.html', locals())

    def post(self, request):
        cadastroForm = self.tipoForm(request.POST)
        if cadastroForm.is_valid():
            cadastro_object = cadastroForm.save()
            sucesso = True
            cadastroForm = self.tipoForm()
        return render(request, 'cadastro.html', locals())


# CARREGAR templates de forma simples:
class carregarTemplate1(View):
    def get(self, request, *args, **kwargs):
        render(request, 'home.html')

# Eh equivalente a:
class carregarTemplate2(TemplateView):
    template_name = 'home.html'
 
# Para passar parâmetros direto da url para que apareçam na template:
class carregarTemplate3(TemplateView):
    template_name = 'home.html'
    name = None
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['name'] = self.name
        return context


class CadastrarGV(CreateView):
    model = Docente
    fields = ['nome', 'nUSP']
    success_url = reverse_lazy('cadastrar gv')


class ListarGV(ListView):
    model = Docente


class EditarGV(UpdateView):
    model = Docente
    fields = ['nome', 'nUSP']
    success_url = reverse_lazy('listar gv')


class DeletarGV(DeleteView):
    model = Docente
    success_url = reverse_lazy('cadastrar gv')
