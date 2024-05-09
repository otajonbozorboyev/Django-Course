from django.shortcuts import render
from about.models import About
from collection.models import Collection
from .models import Blog, Category, Tag


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
    about = About.objects.all()
    blog = Blog.objects.get(id=pk)
    context = {
        'blogs': blog,
        'abouts': about
    }
    return render(request, 'single.html', context)
