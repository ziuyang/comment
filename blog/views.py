from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})


def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/blog/'+str(blog.id))
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update.html', {'form': form})


def delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('home')
