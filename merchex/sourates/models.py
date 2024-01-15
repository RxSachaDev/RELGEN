# sourates/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Title(models.Model):
    name = models.fields.CharField(max_length=3000)
    verset = models.fields.CharField(max_length=5000)
    n_verset = models.fields.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(286)]    
    )  
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