from django.shortcuts import render

from blog.forms import CategoriaForm
from blog.models import Categoria


def inserir_categoria(request):
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            categoria = Categoria(nome=nome)
            categoria.save()
            form = CategoriaForm()
    context = {
        'form': form
    }
    return render(request, 'inserir_categoria.html', context)
