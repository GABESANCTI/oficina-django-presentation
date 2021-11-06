from django.urls import path

from blog.views import inserir_categoria

urlpatterns = [
    path('inserir_categoria/', inserir_categoria, name='inserir_categoria'),
]