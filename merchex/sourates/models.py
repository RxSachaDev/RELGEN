# sourates/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.utils import timezone


class Christ(models.Model):
    name = models.fields.CharField(max_length=3000)
    section = models.fields.CharField(max_length=3000)
    verset = models.fields.CharField(max_length=5000)
    n_chap = models.fields.IntegerField(default = 1)
    n_verset = models.fields.IntegerField(default = 1)
    
    def __str__(self):
        return f'{self.name}'

class Sourate(models.Model):
    name = models.fields.CharField(max_length=3000)
    verset = models.fields.CharField(max_length=5000)
    n_verset = models.fields.IntegerField( 
    )  
    def __str__(self):
        return f'{self.name}'
    
class Juda(models.Model):
    name = models.fields.CharField(max_length=3000)
    verset = models.fields.CharField(max_length=5000)
    n_verset = models.fields.IntegerField(default = 1)
    n_chap = models.fields.IntegerField(default = 1)
    def __str__(self):
        return f'{self.name}'

class Date(models.Model):
    date_jour = models.DateField()
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghreb = models.TimeField()
    icha = models.TimeField()   
    def __str__(self):
        return self.date_jour.strftime('%Y-%m-%d')

class Date2(models.Model):
    annee = models.IntegerField(default=2024)
    epiphanie = models.DateField()
    chandeleur = models.DateField()
    careme = models.DateField()
    mercredi = models.DateField()
    paques = models.DateField()
    ascension = models.DateField()
    pentecote = models.DateField()
    fete = models.DateField()
    toussaint = models.DateField()
    noel = models.DateField()
    pourim = models.DateField(default=date.today)
    pessah = models.DateField(default=date.today)
    chavouot = models.DateField(default=date.today)
    roch = models.DateField(default=date.today)
    yom = models.DateField(default=date.today)
    souccot = models.DateField(default=date.today)
    simhat = models.DateField(default=date.today)
    hanouka = models.DateField(default=date.today)
    def __str__(self):
        return str(self.annee)
""
class Chabbat(models.Model):
    debut = models.DateTimeField(default=timezone.now)
    fin = models.DateTimeField()
    def __str__(self):
        return f"{self.debut.strftime('%Y-%m-%d')}"
          
class Contact(models.Model):
    RAISON_CHOICES = [
        ('question', 'Question'),
        ('avis', 'Avis'),
        ('probleme', 'Problème'),
        ('autre', 'Autre'),
    ]
    nom = models.CharField(max_length=40,blank=False)
    mail = models.EmailField(blank=False)
    raison = models.CharField(max_length=20, choices=RAISON_CHOICES, default='question', blank=False)
    message = models.CharField(max_length=500,blank=False)
    def __str__(self):
        return f"{self.nom} - {self.raison}"