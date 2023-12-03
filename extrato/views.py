from .models import Valores
from bancos.models import Banco
from categorias.models import Categoria

from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import constants
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from io import BytesIO
# from weasyprint import HTML

import os



def novo_valor(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {
            'bancos':bancos,
            'categorias':categorias,
        })
    elif request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        banco = request.POST.get('banco')
        tipo = request.POST.get('tipo')
        
        if not data:
            data = datetime.now()
        
        valor_ = Valores(
            banco_id=banco,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            data=data,
            tipo=tipo
        )
        valor_.save()
        
        banco = Banco.objects.get(id=banco)
        
        if tipo =='E':
            banco.saldo += float(valor)
        else:
            banco.saldo -= float(valor)
        banco.save()
        
        messages.add_message(request, constants.INFO, 'Novo valor adicionado ao banco.')
        return redirect('/extrato/novo_valor')


def view_extrato(request):
    if request.method == 'GET':
        bancos = Banco.objects.all()
        categorias = Categoria.objects.all()
        valores = Valores.objects.filter(data__month=datetime.now().month).order_by('-data')
        
        banco_get = request.GET.get('banco')
        categoria_get = request.GET.get('categoria')
        
        if banco_get:
            valores = valores.filter(banco__id=banco_get)
        if categoria_get:
            valores = valores.filter(categoria__id=categoria_get)
        # TODO: botão para zerar os filtros
        # TODO: filtros de período
        
        return render(request, 'view_extrato.html', {
            'bancos':bancos,
            'categorias':categorias,
            'valores':valores
        })


def exportar_pdf(request):
    pass
#     valores = Valores.objects.filter(data__month=datetime.now().month)
#     contas = Conta.objects.all()
#     categorias = Categoria.objects.all()
    
#     path_template = os.path.join(settings.BASE_DIR, 'templates/partials/extrato.html')
#     path_output = io.BytesIO()
    
#     template_render = render_to_string(path_template, {
#         'valores':valores,
#         'contas':contas,
#         'categorias':categorias
#     })
#     HTML(string=template_render).write_pdf(path_output)
    # https://pygobject.readthedocs.io/en/latest/getting_started.html#macosx-getting-started
    # path_output.seek(0)
    # return FileResponse(path_output, filename='extrato.pdf')
