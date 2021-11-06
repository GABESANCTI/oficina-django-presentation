from django.urls import path

from blog.views import inserir_categoria, visualizar_categorias

urlpatterns = [
    path('inserir_categoria/', inserir_categoria, name='inserir_categoria'),
    path('visualizar_categorias/', visualizar_categorias, name='visualizar_categorias'),
]