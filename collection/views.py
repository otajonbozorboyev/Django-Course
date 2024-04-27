from django.shortcuts import render

def collectionView(request):
    return render(request, 'collection.html')