# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *

# Create your views here.

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

# Exemplo de CBV e seus métodos internos para cada método HTTP
class login_fofo(View):

    def get(self,request):
        return render(request,'login.html',locals())

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        conta_invalida = False

        if user is not None:
            conta_desabilitada = False
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                conta_desabilitada = True
        else:
            conta_invalida = True
        return render(request, 'login.html', locals())

# Exemplo de CBVs com herança e aproveitamento de código para diferentes classes de objetos
class Cadastro(View):
    # tipoForm é reescrito na chamada da url para o tipo adequado de acordo com a página anterior
    tipoForm = None

    def get(self, request):
        cadastroForm = self.tipoForm()
    return render(request, 'cadastro.html', locals())

class CadastroUsuarios(Cadastro):
    """docstring for CadastroUsuarios"""
    # Esta classe herda os atributos e métodos da mãe e pode reescrever algumas características
    novo_atributo = "xablau"
    def get(self, request):
        # Aqui fazemos rotinas a mais
        user_form = UserForm()  # Usuários possum um form de User
        #
        # Podemos chamar atributos desta classe ou da mãe utilizando self
        mais_novo_atributo= self.novo_atributo
        atributo_mae = self.tipoForm
        #
        # Sem o uso do self, estaríamos tentando chamar atributos que não existem
        vai_dar_erro = novo_atributo
        #
        # Chamada de método get() da classe Mãe. Reparem na necessidade de se usar super(ClassName, args).<method>
        super(Cadastro, self).get()
