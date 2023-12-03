from .utils import calcula_total, calcula_equilibrio_financeiro, contagem_total
from contas.models import ContaPaga, ContaPagar
from extrato.models import Valores
from bancos.models import Banco
from categorias.models import Categoria

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.shortcuts import render, redirect



def home(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        valores = Valores.objects.all()
        valores_mensais = Valores.objects.filter(data__month = datetime.now().month)
        entradas = valores.filter(tipo='E')
        entradas_mensais = valores_mensais.filter(tipo='E')
        saidas = valores.filter(tipo='S')
        saidas_mensais = valores_mensais.filter(tipo='S')
        total_bancos = 0
        
        for banco in bancos:
            total_bancos += banco.saldo
            
        total_entradas = calcula_total(entradas, 'valor')
        total_saidas = calcula_total(saidas, 'valor')
        saldo_total = total_entradas - total_saidas
        
        total_entradas_mensais = calcula_total(entradas_mensais, 'valor')
        total_saidas_mensais = calcula_total(saidas_mensais, 'valor')
        saldo_mensal = total_entradas_mensais - total_saidas_mensais
        
        mes_atual = datetime.now().month
        dia_atual = datetime.now().day
        
        contas_a_pagar = ContaPagar.objects.all()
        
        contas_pagas = ContaPaga.objects\
            .filter(data_pagamento__month=mes_atual)\
                .values('conta')
        contas_vencidas = contas_a_pagar\
            .filter(dia_pagamento__lt = dia_atual)\
                .exclude(id__in=contas_pagas)
        contas_proximas_vencimento = contas_a_pagar\
            .filter(dia_pagamento__lte = dia_atual + 5)\
                .filter(dia_pagamento__gte = dia_atual)\
                    .exclude(id__in=contas_pagas)
        
        contagem_contas_vencidas = contagem_total(contas_vencidas)
        contagem_contas_proximas_vencimento = contagem_total(contas_proximas_vencimento)
        
        percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()
        
        return render(request, 'home.html', {
            'bancos':bancos,
            'valores':valores,
            'entradas':entradas,
            'saidas':saidas,
            'total_entradas':total_entradas,
            'total_saidas':total_saidas,
            'saldo_total':saldo_total,
            'total_entradas_mensais':total_entradas_mensais,
            'total_saidas_mensais':total_saidas_mensais,
            'saldo_mensal':saldo_mensal,
            'contagem_contas_vencidas':contagem_contas_vencidas,
            'contagem_contas_proximas_vencimento':contagem_contas_proximas_vencimento,
            'percentual_gastos_essenciais':int(percentual_gastos_essenciais),
            'percentual_gastos_nao_essenciais':int(percentual_gastos_nao_essenciais),
        })
        
    elif request.method == 'POST':
        pass