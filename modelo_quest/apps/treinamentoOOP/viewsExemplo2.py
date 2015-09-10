# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *

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
