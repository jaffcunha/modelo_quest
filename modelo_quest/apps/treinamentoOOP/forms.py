# -*- coding: utf-8 -*-
from django import forms 
from modelo_quest.apps.treinamentoOOP.models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome',]
        abstract = True

class DocenteForm(UsuarioForm):
    class Meta:
        model = Docente
        fields = UsuarioForm.Meta.fields + ['nUSP',]
