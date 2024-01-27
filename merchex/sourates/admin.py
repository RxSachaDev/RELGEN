from django.contrib import admin
from sourates.models import Christ
from sourates.models import Sourate
from sourates.models import Date
from sourates.models import Date2

class ChristAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'section', 'n_verset') # liste les champs que nous voulons sur l'affichage de la liste

class SourateAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'n_verset')

class Date2Admin(admin.ModelAdmin):
    pass          

admin.site.register(Christ, ChristAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Sourate, SourateAdmin)
admin.site.register(Date)
admin.site.register(Date2)