# -*- coding: utf-8 -*-
from django import forms 
from modelo_quest.apps.treinamentoOOP.models import *

class PesquisadorForm(forms.ModelForm):
    class Meta:
        model = Pesquisador
        fields = ['nome',]
        abstract = True

class DocenteForm(PesquisadorForm):
    class Meta:
        model = Docente
        fields = PesquisadorForm.Meta.fields + ['nUSP',]
