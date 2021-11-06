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


def visualizar_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'visualizar_categorias.html', context)


def editar_categoria(request, id):
    categoria_original = Categoria.objects.get(id=id)
    form = CategoriaForm(request.POST or None, instance=categoria_original)
    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            categoria_original.nome = nome
            categoria_original.save(force_update=True)
    context = {
        'form': form,
    }
    return render(request, 'editar_categoria.html', context)
