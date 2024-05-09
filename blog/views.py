from django.shortcuts import render, redirect
from about.models import About
from collection.models import Collection
from .models import Blog, Category, Tag
from .forms import CommentForm

def indexView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    context = {
        'abouts': about,
        'collections': collection
    }
    return render(request, 'index.html', context)


def blogView(request):
    about = About.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.all().order_by('-id')
    context = {
        'abouts': about,
        'categories': category,
        'tags': tag,
        'blogs': blog
    }
    return render(request, 'blog.html', context)


def detailView(request, pk):
    blog1 = Blog.objects.all().order_by('-id')
    about = About.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.get(id=pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
        'blog1': blog1,
        'blogs': blog,
        'abouts': about,
        'categories': category,
        'tags': tag,
        'form': form
    }
    return render(request, 'single.html', context)
