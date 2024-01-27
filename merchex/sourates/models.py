# sourates/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Christ(models.Model):
    name = models.fields.CharField(max_length=3000)
    section = models.fields.CharField(max_length=3000)
    verset = models.fields.CharField(max_length=5000)
    n_verset = models.fields.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(1292)]    
    )
    def __str__(self):
        return f'{self.name}'

class Sourate(models.Model):
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