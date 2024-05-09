from django.shortcuts import render
from about.models import About
from .models import Collection


def collectionView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    context = {
        'abouts': about,
        'collections': collection
    }
    return render(request, 'collection.html', context)
