from bancos.models import Banco
from categorias.models import Categoria
from contas.models import ContaPaga, ContaPagar
from extrato.models import Valores

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.shortcuts import render, redirect



def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()
    
    for categoria in categorias:
        dados[categoria.categoria] = Valores.objects\
            .filter(categoria=categoria)\
                .aggregate(Sum('valor'))['valor__sum']
    print(dados.keys())
    print(dados.values())
    return render(request, 'dashboard.html', {
        'labels':list(dados.keys()),
        'values':list(dados.values()),
    })
