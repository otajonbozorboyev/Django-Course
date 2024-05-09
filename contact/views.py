from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMe
from about.models import About

def contactView(request):
    about = About.objects.all()
    contactme = ContactMe.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts': about,
        'me': contactme,
        'form': form,
    }
    return render(request, 'contact.html', context)