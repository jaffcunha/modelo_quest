# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from modelo_quest.apps.treinamentoOOP.models import *
from modelo_quest.apps.treinamentoOOP.views import *
from modelo_quest.apps.treinamentoOOP.forms import *

urlpatterns = patterns('',
    url(r'^$', ListarDocente.as_view(), name='list_notes'),
    url(r'^cadastrarCBV/$', Cadastro.as_view(tipoForm = DocenteForm), name='create_note'),
    url(r'^cadastrarGV/$', CadastrarDocente.as_view(), name='create_note'),
    # url(r'^edit/(?P<pk>\d+)/$', EditNote.as_view(), name='edit_note'),
    # url(r'^delete/(?P<pk>\d+)/$', DeleteNote.as_view(), name='delete_note'),
)
