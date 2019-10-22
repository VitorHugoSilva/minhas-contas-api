from django.db import models

from minhascontas.models import TipoConta


class Conta(models.Model):
    nome = models.CharField(max_length=255)
    tipo_conta = models.ForeignKey(TipoConta, on_delete=models.PROTECT, related_name='tipo_contas', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
