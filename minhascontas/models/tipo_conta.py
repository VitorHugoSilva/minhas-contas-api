from django.db import models


class TipoConta(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='users', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)