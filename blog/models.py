from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=40)
