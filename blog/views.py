from django.shortcuts import render

from blog.forms import CategoriaForm


def inserir_categoria(request):
    form = CategoriaForm()
    context = {
        'form': form
    }
    return render(request, 'inserir_categoria.html', context)
