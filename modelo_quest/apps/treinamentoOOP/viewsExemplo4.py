# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *

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
