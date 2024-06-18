from django.shortcuts import render, redirect
from blog.forms import PostForm
from blog.models import Post


def posts(request):
    post_list = Post.objects.all()

    return render(request, 'posts.html', {
        'posts': post_list
    })


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

    return render(request, 'create_update_form.html',{
        'form': form,
        'title': 'Crear nueva noticia',
        'submit_value': 'Publicar noticia',
        'button_style': 'is-primary'

    })


def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'create_update_form.html', {
        'form': form,
        'title': f'Noticia: {post.title}',
        'submit_value': 'Editar noticia',
        'button_style': 'is-warning'
    })


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    post.delete()
    return redirect('home')