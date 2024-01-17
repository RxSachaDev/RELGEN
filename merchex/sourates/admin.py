from django.contrib import admin
from sourates.models import Band
from sourates.models import Sourate
from sourates.models import Date

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class SourateAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'n_verset')

          

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Sourate, SourateAdmin)
admin.site.register(Date)