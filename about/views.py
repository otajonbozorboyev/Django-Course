from django.shortcuts import render
from .models import About
from collection.models import Collection

def aboutView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    context = {
        'abouts': about,
        'collections': collection,
    }
    return render(request, 'about.html', context)