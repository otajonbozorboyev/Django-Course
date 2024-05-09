from django.shortcuts import render, redirect
from .forms import ContactForm
from blog.models import Blog, Category
from .models import ContactMe
from about.models import About

def contactView(request):
    about = About.objects.all()
    contactme = ContactMe.objects.all()
    form = ContactForm(request.POST or None)
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts': about,
        'me': contactme,
        'form': form,        
        'blogs': blog,
        'categories': category,
    }
    return render(request, 'contact.html', context)