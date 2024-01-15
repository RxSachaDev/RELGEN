# ~/projects/django-web-app/merchex/sourates/views.py

from django.http import HttpResponse
from django.shortcuts import render
from sourates.models import Band
from sourates.models import Title
from sourates.models import Date
from sourates.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
import random
from datetime import *


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

    date = Date.objects.all()

    current_time = datetime.now().time()
    
    Fajr =  datetime.combine(datetime.today(), date[0].fajr) - datetime.combine(datetime.today(), current_time)

    fajr_hours = Fajr.seconds // 3600

    fajr_minutes = (Fajr.seconds % 3600) // 60

    fajr_seconds = (Fajr.seconds % 3600) % 60

    Maghreb =  datetime.combine(datetime.today(), date[0].maghreb) - datetime.combine(datetime.today(), current_time)

    maghreb_hours = Maghreb.seconds // 3600

    maghreb_minutes = (Maghreb.seconds % 3600) // 60

    maghreb_seconds = (Maghreb.seconds % 3600) % 60

    Dhuhr =  datetime.combine(datetime.today(), date[0].dhuhr) - datetime.combine(datetime.today(), current_time)

    dhuhr_hours = Dhuhr.seconds // 3600

    dhuhr_minutes = (Dhuhr.seconds % 3600) // 60

    dhuhr_seconds = (Dhuhr.seconds % 3600) % 60

    Asr =  datetime.combine(datetime.today(), date[0].asr) - datetime.combine(datetime.today(), current_time)

    asr_hours = Asr.seconds // 3600

    asr_minutes = (Asr.seconds % 3600) // 60

    asr_seconds = (Asr.seconds % 3600) % 60

    Icha =  datetime.combine(datetime.today(), date[0].icha) - datetime.combine(datetime.today(), current_time)

    icha_hours = Icha.seconds // 3600

    icha_minutes = (Icha.seconds % 3600) // 60

    icha_seconds = (Icha.seconds % 3600) % 60

    return render(request, 'sourates/sourates.html', {'title': title,  'fajr_hours' : fajr_hours, 'fajr_minutes' : fajr_minutes, 'fajr_seconds' : fajr_seconds, 'maghreb_hours' : maghreb_hours, 'maghreb_minutes' : maghreb_minutes, 'maghreb_seconds' : maghreb_seconds, 'dhuhr_hours' : dhuhr_hours, 'dhuhr_minutes' : dhuhr_minutes, 'dhuhr_seconds' : dhuhr_seconds, 'asr_hours' : asr_hours, 'asr_minutes' : asr_minutes, 'asr_seconds' : asr_seconds, 'icha_hours' : icha_hours, 'icha_minutes' : icha_minutes, 'icha_seconds' : icha_seconds } )

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
