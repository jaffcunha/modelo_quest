# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *
from modelo_quest.apps.treinamentoOOP.forms import *
from vanilla import CreateView, DeleteView, ListView, DetailView, UpdateView, TemplateView

class CadastrarGV(CreateView):
    model = Docente
    form_class = DocenteForm
    success_url = reverse_lazy('cadastrar gv')

    def form_valid(self, form):
        docente = form.save(commit=False)
        docente.user = self.request.user
        return super(CadastrarGV, self).form_valid(form)