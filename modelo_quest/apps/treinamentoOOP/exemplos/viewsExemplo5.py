# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *
from modelo_quest.apps.treinamentoOOP.forms import *
from vanilla import CreateView, DeleteView, ListView, DetailView, UpdateView, TemplateView
from django.contrib.auth.models import User


# Models.py
class Usuario(models.Model):
    """docstring for Usuário"""
    nome = models.CharField(max_length=64)
    user = OneToOneField(User, null =True, blank=True)


# Forms.py
class UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ["username","password"]


class UsuarioForm(UserForm):
    

    class Meta:
        model = Usuario
        fields = UserForm.Meta.fields + ['nome',]
        abstract = True
