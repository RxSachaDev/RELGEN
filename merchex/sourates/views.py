# ~/projects/django-web-app/merchex/sourates/views.py

from django.http import HttpResponse
from django.shortcuts import render
from sourates.models import Christ
from sourates.models import Sourate
from sourates.models import Date
from sourates.models import Date2
from sourates.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
import random
from datetime import *
from datetime import date
from sourates.models import Juda


def christ_list(request):
    christs = Christ.objects.all().order_by('?')[:1]
    christ = christs[0]
    date_objects = Date2.objects.all()

    now = datetime.now().date()

    i = 0
    while i < len(date_objects) and date_objects[i].annee != now.year:
        i += 1

    if i < len(date_objects):
        time_difference = date_objects[i].epiphanie - now

        if time_difference.days < 0:
            Epiphanie = date_objects[i + 1].epiphanie - now
            Epiphanie = Epiphanie.days
        else:
            Epiphanie = time_difference.days

        time_difference2 = date_objects[i].chandeleur - now

        if time_difference2.days < 0:
            Chandeleur = date_objects[i + 1].chandeleur - now
            Chandeleur = Chandeleur.days
        else:
            Chandeleur = time_difference2.days

        time_difference3 = date_objects[i].careme - now

        if time_difference3.days < 0:
            Careme = date_objects[i + 1].careme - now
            Careme = Careme.days
        else:
            Careme = time_difference3.days

        time_difference4 = date_objects[i].mercredi - now

        if time_difference4.days < 0:
            Mercredi = date_objects[i + 1].mercredi - now
            Mercredi = Mercredi.days
        else:
            Mercredi = time_difference4.days

        time_difference5 = date_objects[i].paques - now

        if time_difference5.days < 0:
            Paques = date_objects[i + 1].paques - now
            Paques = Paques.days
        else:
            Paques = time_difference5.days

        time_difference6 = date_objects[i].ascension - now

        if time_difference6.days < 0:
            Ascension = date_objects[i + 1].ascension - now
            Ascension = Ascension.days
        else:
            Ascension = time_difference6.days

        time_difference7 = date_objects[i].pentecote - now

        if time_difference7.days < 0:
            Pentecote = date_objects[i + 1].pentecote - now
            Pentecote = Pentecote.days
        else:
            Pentecote = time_difference7.days

        time_difference8 = date_objects[i].fete - now

        if time_difference8.days < 0:
            Fete = date_objects[i + 1].fete - now
            Fete = Fete.days
        else:
            Fete = time_difference8.days

        time_difference9 = date_objects[i].toussaint - now

        if time_difference9.days < 0:
            Toussaint = date_objects[i + 1].toussaint - now
            Toussaint = Toussaint.days
        else:
            Toussaint = time_difference9.days

        time_difference10 = date_objects[i].noel - now

        if time_difference10.days < 0:
            Noel = date_objects[i + 1].noel - now
            Noel = Noel.days
        else:
            Noel = time_difference10.days

        


    return render(request, 'sourates/christiannisme.html', {'christ': christ, 'Epiphanie': Epiphanie, 'Pentecote': Pentecote, 'Fete': Fete, 'Toussaint': Toussaint, 'Noel':Noel, 'Ascension': Ascension, 'Chandeleur': Chandeleur, 'Careme': Careme, 'Mercredi': Mercredi, 'Paques': Paques})

def juda(request):
    juda = Juda.objects.all().order_by('?')[:1]
    juda = juda[0]
    return render(request,'sourates/judaisme.html', {'juda': juda})

def about(request):
    return render(request,'sourates/accueil.html')


def sourates(request):
    # Récupérer tous les objets Sourate et les ordonner de manière aléatoire
    sourates = Sourate.objects.all().order_by('?')[:1]

    # S'assurer qu'il y a au moins un titre
    sourate = sourates[0]

    date = Date.objects.all()

    now = datetime.now()

    current_time = datetime.now().time()

    

    i = 0
    while i < len(date) and (date[i].date_jour.year != now.year or date[i].date_jour.day != now.day or date[i].date_jour.month != now.month):
        i += 1

    if i < len(date):
        time_difference = datetime.combine(datetime.today(), date[i].fajr) - datetime.combine(datetime.today(), current_time)

        if time_difference.total_seconds() < 0:
            Fajr = datetime.combine(datetime.today(), date[i+1].fajr) - datetime.combine(datetime.today(), current_time)
        else:
            Fajr = time_difference


        fajr_hours = Fajr.seconds // 3600

        fajr_minutes = (Fajr.seconds % 3600) // 60

        fajr_seconds = (Fajr.seconds % 3600) % 60

        time_difference2 = datetime.combine(datetime.today(), date[i].maghreb) - datetime.combine(datetime.today(), current_time)

        if time_difference2.total_seconds() < 0:
            Maghreb = datetime.combine(datetime.today(), date[i+1].maghreb) - datetime.combine(datetime.today(), current_time)
        else:
            Maghreb = time_difference2

        maghreb_hours = Maghreb.seconds // 3600

        maghreb_minutes = (Maghreb.seconds % 3600) // 60

        maghreb_seconds = (Maghreb.seconds % 3600) % 60

        time_difference3 = datetime.combine(datetime.today(), date[i].dhuhr) - datetime.combine(datetime.today(), current_time)

        if time_difference3.total_seconds() < 0:
            Dhuhr = datetime.combine(datetime.today(), date[i+1].dhuhr) - datetime.combine(datetime.today(), current_time)
        else:
            Dhuhr = time_difference3


        dhuhr_hours = Dhuhr.seconds // 3600

        dhuhr_minutes = (Dhuhr.seconds % 3600) // 60

        dhuhr_seconds = (Dhuhr.seconds % 3600) % 60

        time_difference4 = datetime.combine(datetime.today(), date[i].asr) - datetime.combine(datetime.today(), current_time)

        if time_difference4.total_seconds() < 0:
            Asr = datetime.combine(datetime.today(), date[i+1].asr) - datetime.combine(datetime.today(), current_time)
        else:
            Asr = time_difference4


        asr_hours = Asr.seconds // 3600

        asr_minutes = (Asr.seconds % 3600) // 60

        asr_seconds = (Asr.seconds % 3600) % 60

        time_difference5 = datetime.combine(datetime.today(), date[i].icha) - datetime.combine(datetime.today(), current_time)

        if time_difference5.total_seconds() < 0:
            Icha = datetime.combine(datetime.today(), date[i+1].icha) - datetime.combine(datetime.today(), current_time)
        else:
            Icha = time_difference5


        icha_hours = Icha.seconds // 3600

        icha_minutes = (Icha.seconds % 3600) // 60

        icha_seconds = (Icha.seconds % 3600) % 60

    return render(request, 'sourates/sourates.html', {'sourate': sourate,  'fajr_hours' : fajr_hours, 'fajr_minutes' : fajr_minutes, 'fajr_seconds' : fajr_seconds, 'maghreb_hours' : maghreb_hours, 'maghreb_minutes' : maghreb_minutes, 'maghreb_seconds' : maghreb_seconds, 'dhuhr_hours' : dhuhr_hours, 'dhuhr_minutes' : dhuhr_minutes, 'dhuhr_seconds' : dhuhr_seconds, 'asr_hours' : asr_hours, 'asr_minutes' : asr_minutes, 'asr_seconds' : asr_seconds, 'icha_hours' : icha_hours, 'icha_minutes' : icha_minutes, 'icha_seconds' : icha_seconds } )

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
