from django.shortcuts import render
from blog.models import Blog, Category
from about.models import About
from .models import Service
from contact.models import ContactMe


def serviceView(request):
    service = Service.objects.all()
    about = About.objects.all()
    contactme = ContactMe.objects.all()    
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,        
        'services': service,
        'me': contactme,
        'blogs': blog,
        'categories': category,
    }
    return render(request, 'services.html', context)