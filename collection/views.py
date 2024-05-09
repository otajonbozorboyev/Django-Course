from django.shortcuts import render
from blog.models import Blog, Category
from about.models import About
from contact.models import ContactMe
from .models import Collection


def collectionView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    contactme = ContactMe.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,
        'me': contactme,
        'blogs': blog,
        'categories': category,
        'collections': collection,

    }
    return render(request, 'collection.html', context)
