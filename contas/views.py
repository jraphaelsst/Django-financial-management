from .models import ContaPaga, ContaPagar
from bancos.models import Banco
from categorias.models import Categoria

from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render



def definir_despesas(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render(request, 'definir_despesas.html', {
            'categorias':categorias,
        })
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')
        
        conta_a_pagar = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento
        )
        conta_a_pagar.save()
        
        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso.')
        return redirect('/contas/definir_contas')


def ver_despesas(request):
    if request.method == 'GET':
        mes_atual = datetime.now().month
        dia_atual = datetime.now().day
        
        contas = ContaPagar.objects.all()
        
        contas_pagas = ContaPaga.objects\
            .filter(data_pagamento__month=mes_atual)\
                .values('conta')
                
        contas_vencidas = contas\
            .filter(dia_pagamento__lt = dia_atual)\
                .exclude(id__in=contas_pagas)
                
        contas_proximas_vencimento = contas\
            .filter(dia_pagamento__lte = dia_atual + 5)\
                .filter(dia_pagamento__gte = dia_atual)\
                    .exclude(id__in=contas_pagas)
                    
        restantes = contas\
            .exclude(id__in=contas_vencidas)\
                .exclude(id__in=contas_pagas)\
                    .exclude(id__in = contas_proximas_vencimento)
        
        return render(request, 'ver_contas.html', {
            'contas_vencidas':contas_vencidas,
            'contas_proximas_vencimento':contas_proximas_vencimento,
            'restantes':restantes
        })


def apagar_despesa(request, id):
    conta = ContaPagar.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.INFO, 'Conta apagada com sucesso.')
    return redirect('/contas/ver_contas/')