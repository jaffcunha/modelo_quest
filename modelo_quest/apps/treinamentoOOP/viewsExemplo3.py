# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from treinametoOOP.models import *


class ListarCBV(View):
    tipoForm = None
    
    def get(self, request):
        lista = self.tipoForm.Meta.model.objects.all()
        return render(request, "lista.html", locals())
