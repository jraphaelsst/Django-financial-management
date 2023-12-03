from .models import Banco
from categorias.models import Categoria
from extrato.models import Valores

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect



def gerenciar_bancos(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        categorias = Categoria.objects.all()
        total_bancos = 0
        
        for banco in bancos:
            total_bancos += banco.saldo
        
        return render(request, 'gerenciar_bancos.html', {
            'bancos':bancos,
            'categorias':categorias,
            'total_bancos':total_bancos,
        })
        
    elif request.method == 'POST':
        pass


def cadastrar_banco(request):
    data = datetime.now()
    banco = request.POST.get('banco')
    apelido = request.POST.get('apelido')
    tipo = request.POST.get('tipo')
    saldo = request.POST.get('saldo')
    icone = request.POST.get('icone')
    
    if len(apelido.strip()) == 0 or len(str(saldo).strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Por favor, preencha as informações necessárias.')
        return redirect('/perfil/gerenciar/')
    
    categorias = Categoria.objects.all()
    categoria_deposito = categorias.filter(categoria='Depósito')
    
    if categoria_deposito:
        categoria_deposito = categoria_deposito[0]
        
        banco_ = Banco(
            banco=banco,
            apelido=apelido,
            tipo=tipo,
            saldo=0,
        )
        banco_.save()
        
        valor_ = Valores(
            banco_id=banco_.id,
            categoria_id=categoria_deposito.id,
            descricao='Depósito Inicial',
            valor=saldo,
            tipo='E'
        )
        valor_.save()
        
        banco_ = Banco.objects.get(id=banco_.id)
        if valor_.tipo == 'E':
            banco_.saldo += float(valor_.valor)
        else:
            banco_.saldo -= float(valor_.valor)
        banco_.save()
    
    if not categoria_deposito:
        categoria_ = Categoria(
            categoria='Depósito',
            essencial=True,
            valor_planejamento=saldo,
        )
        categoria_.save()
        
        categorias = Categoria.objects.all()
        categoria_deposito = categorias.filter(categoria='Depósito')

        banco_ = Banco(
            banco=banco,
            apelido=apelido,
            tipo=tipo,
            saldo=0,
        )
        banco_.save()
        
        valor_ = Valores(
            banco_id=banco_.id,
            categoria_id=categoria_deposito[0].id,
            descricao='Depósito Inicial',
            valor=saldo,
            tipo='E'
        )
        valor_.save()
        
        banco_ = Banco.objects.get(id=banco_.id)
        if valor_.tipo == 'E':
            banco_.saldo += float(valor_.valor)
        else:
            banco_.saldo -= float(valor_.valor)
        banco_.save()
        
        messages.add_message(request, constants.SUCCESS, 'Banco cadastrado com sucesso!')
        return redirect('/perfil/gerenciar/')


def deletar_banco(request, id):
    banco_ = Banco.objects.get(id=id)
    banco_.delete()
    
    messages.add_message(request, constants.INFO, 'Conta apagada com sucesso.')
    return redirect('/perfil/gerenciar/')
