# ~/projects/django-web-app/merchex/sourates/views.py

from django.http import HttpResponse
from django.shortcuts import render
from sourates.models import Band
from sourates.models import Title
from sourates.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
import random


def band_list(request):
    bands = Band.objects.all()
    return render(request,
        'sourates/band_list.html',
        {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id) 
  return render(request,
          'sourates/band_detail.html',
          {'band': band})

def about(request):
    return render(request,'sourates/about.html')

def sourates(request):
    # Récupérer tous les objets Title et les ordonner de manière aléatoire
    titles = Title.objects.all().order_by('?')[:1]

    # S'assurer qu'il y a au moins un titre
    title = titles[0]

    return render(request, 'sourates/sourates.html', {'title': title})

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent')   
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'sourates/contact.html',
                {'form': form})

def emailsent(request):
    return render(request,'sourates/emailsent.html')
