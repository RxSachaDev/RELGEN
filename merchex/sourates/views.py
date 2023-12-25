# ~/projects/django-web-app/merchex/sourates/views.py

from django.http import HttpResponse
from django.shortcuts import render
from sourates.models import Band
from sourates.models import Title


def hello(request):
    bands = Band.objects.all()
    return render(request,
        'sourates/hello.html',
        {'bands': bands})

def about(request):
    return render(request,'sourates/about.html')

def sourates(request):
    titles = Title.objects.all()
    return render(request,'sourates/sourates.html', {'titles' : titles})

def contact(request):
    return render(request,'sourates/contact.html')