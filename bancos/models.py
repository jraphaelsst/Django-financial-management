from django.db import models



class Banco(models.Model):
    banco = models.CharField(max_length=30)
    # perfil = models.CharField(max_length=2)
    apelido = models.CharField(max_length=30)
    tipo = models.CharField(max_length=2)
    saldo = models.FloatField()
    # icone = ImageField()
    
    def __str__(self):
        return self.banco
