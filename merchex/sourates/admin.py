from django.contrib import admin
from sourates.models import Christ
from sourates.models import Sourate
from sourates.models import Date
from sourates.models import Date2
from sourates.models import Juda
from sourates.models import Chabbat


class ChristAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'section', 'n_chap', 'n_verset') # liste les champs que nous voulons sur l'affichage de la liste

class SourateAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'n_verset')

class JudaAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'n_chap', 'n_verset')        

admin.site.register(Christ, ChristAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Sourate, SourateAdmin)
admin.site.register(Juda, JudaAdmin)
admin.site.register(Date)
admin.site.register(Date2)
admin.site.register(Chabbat)