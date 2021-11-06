from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField(Categoria, related_name='posts')

    def __str__(self):
        return self.titulo
