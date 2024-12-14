from django.contrib import admin
from listings.models import Band
from listings.models import Liste

#admin.site.register(Band) # Enregistrement du modèle Band 


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed')  # Exemple de configuration de Band

admin.site.register(Band, BandAdmin)  # Registre avec la classe personnalisée

class ListeAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  # Exemple de configuration de Liste

admin.site.register(Liste, ListeAdmin)  # Registre avec la classe personnalisée

from .models import Livre, Etudiant

class LivreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix_unitaire', 'quantite', 'date_creation')  # Exemple de champs

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance', 'livre')  # Exemple de champs

admin.site.register(Livre, LivreAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
