from bancos.models import Banco
from categorias.models import Categoria

from datetime import datetime
from django.db import models



class Valores(models.Model):
    data = models.DateField(default=datetime.now())
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    valor = models.FloatField()
    descricao = models.TextField()
    tipo = models.CharField(max_length=1)
    
    def __str__(self):
        return self.descricao
