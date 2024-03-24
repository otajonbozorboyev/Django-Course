from django.shortcuts import render
from django.http import HttpResponse

def blogView(request):
    return HttpResponse("Assalomu alaykum!")