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

class Pesquisador(models.Model):
    """docstring for Pesquisador"""
    nome = models.CharField(max_length=64)

class Docente(Pesquisador):
    """docstring for Docente"""
    nUSP = models.IntegerField("Número USP")
