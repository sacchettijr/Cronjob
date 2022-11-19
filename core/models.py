from django.db import models


class PessoaModel(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
