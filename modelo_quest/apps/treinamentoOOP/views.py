# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from modelo_quest.apps.treinamentoOOP.models import *
from django.views.generic import View #Importar para usar class-based-views (CBV)
from vanilla import CreateView, DeleteView, ListView, UpdateView


class Cadastro(View):
    """docstring for Cadastrar"""
    tipoForm = None

    def get(self, request):
        cadastroForm = self.tipoForm()
        return render(request, 'cadastro.html', locals())


class ListarDocente(ListView):
    model = Docente


class CadastrarDocente(CreateView):
    model = Docente
    fields = ['nome', 'nUSP']
    success_url = reverse_lazy('list_notes')


class EditarDocente(UpdateView):
    model = Docente
    fields = ['nome', 'nUSP']
    success_url = reverse_lazy('list_notes')


class DeletarDocente(DeleteView):
    model = Docente
    success_url = reverse_lazy('list_notes')
