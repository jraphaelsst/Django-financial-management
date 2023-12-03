from bancos.models import Banco
from categorias.models import Categoria
from contas.models import ContaPaga, ContaPagar
from extrato.models import Valores

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.shortcuts import render, redirect



def gerenciar(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        categorias = Categoria.objects.all()
        total_bancos = 0
        
        for banco in bancos:
            total_bancos += banco.saldo
        
        return render(request, 'gerenciar_perfil.html', {
            'bancos':bancos,
            'categorias':categorias,
            'total_bancos':total_bancos,
        })
        
    elif request.method == 'POST':
        pass
