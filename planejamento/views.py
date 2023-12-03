from categorias.models import Categoria

from django.contrib import messages
from django.contrib.messages import constants

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json



def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {
        'categorias':categorias,
    })

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()
    
    return JsonResponse(
        {'status': 'Sucesso'}
    )


def ver_planejamento(request):
    categorias = Categoria.objects.all()
    # TODO: realizar barra com total e sua respectiva porcentagem
    return render(request, 'ver_planejamento.html', {
        'categorias':categorias
    })
