from django.shortcuts import render, redirect

from blog.forms import CategoriaForm, ComentarioForm
from blog.models import Categoria, Post, Comentario


def inserir_categoria(request):
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            categoria = Categoria(nome=nome)
            categoria.save()
            return redirect('visualizar_categorias')
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
            return redirect('visualizar_categorias')
    context = {
        'form': form,
    }
    return render(request, 'editar_categoria.html', context)


def excluir_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()

    return redirect('visualizar_categorias')


def index(request):
    posts = Post.objects.all().order_by('-criado_em')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def visualizar_post(request, pk):
    post = Post.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(post=post)

    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario(
                autor=form.cleaned_data['autor'],
                mensagem=form.cleaned_data['mensagem'],
                post=post
            )
            comentario.save()
            form = ComentarioForm()

    context = {
        'post': post,
        'comentarios': comentarios,
        'form': form
    }
    return render(request, 'visualizar_post.html', context)