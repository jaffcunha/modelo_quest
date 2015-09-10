# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


# class MyModel(models.Model):

    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String

class Usuario(models.Model):
    """docstring for Usuário"""
    nome = models.CharField(max_length=64)

class Docente(Usuario):
    """docstring for Docente"""
    nUSP = models.IntegerField("Número USP")
