# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *

# Exemplo de FBV
def preco_alterar(request):
    if request.method == 'GET':
        preco = Preco_cartao.objects.get(id = id_preco_cartao)
        preco_form = PrecoAlterarForm(instance = preco)

    elif request.method == 'POST':
        preco_form = PrecoAlterarForm(request.POST, instance = preco)
        highlight_error([preco_form])
        if preco_form.is_valid():
            preco = preco_form.save()
            messages.success(request, u'Preço dos cartões alterado com sucesso!')
            return HttpResponseRedirect('/copiadoras_visualizar/')
        else:
            messages.warning(request, u'Insira um número!')
    return render(request, 'preco_alterar.html', locals())
