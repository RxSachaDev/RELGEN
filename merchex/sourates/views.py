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
from django.utils import timezone
from sourates.models import Juda
from sourates.models import Chabbat

def about(request):
    return render(request,'sourates/accueil.html')

def decouverte(request):
    return render(request,'sourates/decouverte.html')

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
            Epiphanie = str(Epiphanie.days) + ' jours'
        else:
            Epiphanie = str(time_difference.days) + ' jours'
            if time_difference.days == 0:
                Epiphanie = "Aujourd'hui"

        time_difference2 = date_objects[i].chandeleur - now

        if time_difference2.days < 0:
            Chandeleur = date_objects[i + 1].chandeleur - now
            Chandeleur = str(Chandeleur.days) + ' jours'
        else:
            Chandeleur = str(time_difference2.days) + ' jours'
            if time_difference2.days == 0:
                Chandeleur = "Aujourd'hui"

        time_difference3 = date_objects[i].careme - now

        if time_difference3.days < 0:
            Careme = date_objects[i + 1].careme - now
            Careme = str(Careme.days) + ' jours'
        else:
            Careme = str(time_difference3.days) + ' jours'
            if time_difference3.days == 0:
                Careme = "Aujourd'hui"

        time_difference4 = date_objects[i].mercredi - now

        if time_difference4.days < 0:
            Mercredi = date_objects[i + 1].mercredi - now
            Mercredi = str(Mercredi.days) + ' jours'
        else:
            Mercredi = str(time_difference4.days) + ' jours'
            if time_difference4.days == 0:
                Mercredi = "Aujourd'hui"

        time_difference5 = date_objects[i].paques - now

        if time_difference5.days < 0:
            Paques = date_objects[i + 1].paques - now
            Paques = str(Paques.days) + ' jours'
        else:
            Paques = str(time_difference5.days) + ' jours'
            if time_difference5.days == 0:
                Paques = "Aujourd'hui"

        time_difference6 = date_objects[i].ascension - now

        if time_difference6.days < 0:
            Ascension = date_objects[i + 1].ascension - now
            Ascension = str(Ascension.days) + ' jours'
        else:
            Ascension = str(time_difference6.days) + ' jours'
            if time_difference6.days == 0:
                Ascension = "Aujourd'hui"

        time_difference7 = date_objects[i].pentecote - now

        if time_difference7.days < 0:
            Pentecote = date_objects[i + 1].pentecote - now
            Pentecote = str(Pentecote.days) + ' jours'
        else:
            Pentecote = str(time_difference7.days) + ' jours'
            if time_difference7.days == 0:
                Pentecote = "Aujourd'hui"

        time_difference8 = date_objects[i].fete - now

        if time_difference8.days < 0:
            Fete = date_objects[i + 1].fete - now
            Fete = str(Fete.days) + ' jours'
        else:
            Fete = str(time_difference8.days) + ' jours'
            if time_difference8.days == 0:
                Fete = "Aujourd'hui"

        time_difference9 = date_objects[i].toussaint - now

        if time_difference9.days < 0:
            Toussaint = date_objects[i + 1].toussaint - now
            Toussaint = str(Toussaint.days) + ' jours'
        else:
            Toussaint = str(time_difference9.days) + ' jours'
            if time_difference9.days == 0:
                Toussaint = "Aujourd'hui"

        time_difference10 = date_objects[i].noel - now

        if time_difference10.days < 0:
            Noel = date_objects[i + 1].noel - now
            Noel = str(Noel.days) + ' jours'
        else:
            Noel = str(time_difference10.days) + ' jours'
            if time_difference10.days == 0:
                Noel = "Aujourd'hui"

        


    return render(request, 'sourates/christiannisme.html', {'christ': christ, 'Epiphanie': Epiphanie, 'Pentecote': Pentecote, 'Fete': Fete, 'Toussaint': Toussaint, 'Noel':Noel, 'Ascension': Ascension, 'Chandeleur': Chandeleur, 'Careme': Careme, 'Mercredi': Mercredi, 'Paques': Paques})

def juda(request):
    juda = Juda.objects.all().order_by('?')[:1]
    juda = juda[0]
    date = Chabbat.objects.all()
    date_objects = Date2.objects.all()
    now = timezone.now()
    now2 = datetime.now().date()
    i = 0
    while i < len(date) and (date[i].fin - now).total_seconds() < 0:
        i = i +1
    if (date[i].debut - now).total_seconds() >= 0:
        chabbat = date[i].debut - now
        if chabbat.days > 0:
            chabbat = "Début : "+str(chabbat.days)+" jour(s) "+str(chabbat.seconds//3600)+"h "+ str((chabbat.seconds%3600)//60)+"min"
        else :
            chabbat = "Début : "+ str(chabbat.seconds//3600)+"h "+ str((chabbat.seconds%3600)//60)+"min "+ str((chabbat.seconds%3600)%60)+"s"
    
    else:
        chabbat = date[i].fin - now
        chabbat = "Fin : "+str(chabbat.seconds//3600)+"h "+ str((chabbat.seconds%3600)//60)+"min"+ str((chabbat.seconds%3600)%60)+"s"

    
    y = 0
    while y < len(date_objects) and date_objects[y].annee != now2.year:
        y += 1

    if y < len(date_objects):
        time_difference = date_objects[y].pessah - now2

        if time_difference.days < 0:
            Pessah = date_objects[y + 1].pessah - now2
            Pessah = str(Pessah.days) + ' jours'
        else:
            Pessah = str(time_difference.days) + ' jours'
            if time_difference.days == 0:
                Pessah = "Aujourd'hui"

        time_difference2 = date_objects[y].chavouot - now2

        if time_difference2.days < 0:
            Chavouot = date_objects[y + 1].chavouot - now2
            Chavouot = str(Chavouot.days) + ' jours'
        else:
            Chavouot = str(time_difference2.days) + ' jours'
            if time_difference2.days == 0:
                Chavouot = "Aujourd'hui"

        time_difference3 = date_objects[y].roch - now2

        if time_difference3.days < 0:
            Roch = date_objects[y + 1].roch - now2
            Roch = str(Roch.days) + ' jours'
        else:
            Roch = str(time_difference3.days) + ' jours'
            if time_difference3.days == 0:
                Roch = "Aujourd'hui"

        time_difference4 = date_objects[y].yom - now2

        if time_difference4.days < 0:
            Yom = date_objects[y + 1].yom - now2
            Yom = str(Yom.days) + ' jours'
        else:
            Yom = str(time_difference4.days) + ' jours'
            if time_difference4.days == 0:
                Yom = "Aujourd'hui"

        time_difference5 = date_objects[y].souccot - now2

        if time_difference5.days < 0:
            Souccot = date_objects[y + 1].souccot - now2
            Souccot = str(Souccot.days) + ' jours'
        else:
            Souccot = str(time_difference5.days) + ' jours'
            if time_difference5.days == 0:
                Souccot = "Aujourd'hui"

        time_difference6 = date_objects[y].simhat - now2

        if time_difference6.days < 0:
            Simhat = date_objects[y + 1].simhat - now2
            Simhat = str(Simhat.days) + ' jours'
        else:
            Simhat = str(time_difference6.days) + ' jours'
            if time_difference6.days == 0:
                Simhat = "Aujourd'hui"

        time_difference7 = date_objects[y].hanouka - now2

        if time_difference7.days < 0:
            Hanouka = date_objects[y + 1].hanouka - now2
            Hanouka = str(Hanouka.days) + ' jours'
        else:
            Hanouka = str(time_difference7.days) + ' jours'
            if time_difference7.days == 0:
                Hanouka = "Aujourd'hui"

        time_difference8 = date_objects[y].pourim - now2

        if time_difference8.days < 0:
            Pourim = date_objects[y + 1].pourim - now2
            Pourim = str(Pourim.days) + ' jours'
        else:
            Pourim = str(time_difference8.days) + ' jours'
            if time_difference8.days == 0:
                Pourim = "Aujourd'hui"
    return render(request,'sourates/judaisme.html', {'juda': juda, 'Chabbat': chabbat, 'Pessah':Pessah,'Chavouot':Chavouot,'Roch':Roch,'Yom':Yom,'Souccot':Souccot,'Simhat':Simhat,'Hanouka':Hanouka,'Pourim':Pourim})


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

def conditions(request):
    return render(request,'sourates/conditions.html')

def mentions(request):
    return render(request,'sourates/mentions.html')

def cookies(request):
    return render(request,'sourates/cookies.html')

