# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from modelo_quest.apps.treinamentoOOP.models import *
from modelo_quest.apps.treinamentoOOP.views import *
from modelo_quest.apps.treinamentoOOP.forms import *
from vanilla import CreateView, DeleteView, ListView, UpdateView, TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^template/$', carregarTemplate3.as_view(name="Jaff Cunha")),
    #
    # CBV
    url(r'^cadastrarCBV/$', CadastrarCBV.as_view(tipoForm=DocenteForm),
        name='cadastrar cbv'),
    # url(r'^listarCBV/$', ListarCBV.as_view(tipoForm=DocenteForm),
    #     name='listar cbv'),
    #  
    # CBGV
    url(r'^cadastrarGV/$', CadastrarGV.as_view(), name='cadastrar gv'),
    url(r'^listarGV/$', ListarGV.as_view(), name='listar gv'),
    url(r'^detalharGV/(?P<pk>\d+)/$', DetalharGV.as_view(),
        name='detalhar gv'),
    url(r'^editarGV/(?P<pk>\d+)/$', EditarGV.as_view(), name='editar gv'),
    url(r'^deletarGV/(?P<pk>\d+)/$', DeletarGV.as_view(), name='deletar gv'),
)
