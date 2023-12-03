from .models import Categoria
from bancos.models import Banco
from extrato.models import Valores

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.shortcuts import render, redirect



def gerenciar_categorias(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        categorias = Categoria.objects.all()
        total_bancos = 0
        
        for banco in bancos:
            total_bancos += banco.saldo
        
        dados = {}
        categorias = Categoria.objects.all()
        
        for categoria in categorias:
            dados[categoria.categoria] = Valores.objects\
                .filter(categoria=categoria)\
                    .aggregate(Sum('valor'))['valor__sum']
        print(dados.keys())
        print(dados.values())
        
        return render(request, 'gerenciar_categorias.html', {
            'bancos':bancos,
            'categorias':categorias,
            'total_bancos':total_bancos,
            'labels':list(dados.keys()),
            'values':list(dados.values()),
        })
        
    elif request.method == 'POST':
        pass


def cadastrar_categoria(request):
    categoria = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))
    
    categoria = Categoria(
        categoria=categoria,
        essencial=essencial,
    )
    categoria.save()
    
    messages.add_message(request, constants.SUCCESS, 'Nova categoria adicionada com sucesso.')
    return redirect('/categorias/gerenciar_categorias/')


def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.essencial = not categoria.essencial
    categoria.save()
    return redirect('/categorias/gerenciar_categorias/')
