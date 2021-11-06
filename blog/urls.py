from django.urls import path

from blog.views import *

urlpatterns = [
    path('inserir_categoria/', inserir_categoria, name='inserir_categoria'),
    path('visualizar_categorias/', visualizar_categorias, name='visualizar_categorias'),
    path('editar_categoria/<int:id>', editar_categoria, name='editar_categoria'),
    path('excluir_categoria/<int:id>', excluir_categoria, name='excluir_categoria'),
]
