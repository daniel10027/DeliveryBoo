from django.contrib import admin
from .models import Colis

class ColisAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'source', 'destination', 'proprietaire', 'contact', 'etat', 'active', 'created', 'date_update', 'code')
    list_filter = ('etat', 'active', 'created', 'date_update')
    search_fields = ('titre', 'proprietaire', 'code')
    list_editable = ('etat', 'active')  # Permet l'édition directe dans la liste
    list_per_page = 20  # Nombre d'objets affichés par page
    date_hierarchy = 'created'  # Ajoute une hiérarchie de date pour la navigation
    ordering = ['created']  # Trie par défaut par date de création
    actions_on_top = True  # Affiche les actions en haut de la liste
    actions_on_bottom = False  # N'affiche pas les actions en bas de la liste
    list_select_related = True  # Effectue une requête de jointure pour les clés étrangères
    save_as = True  # Permet de sauvegarder en tant que nouvelle entrée depuis l'écran de modification

admin.site.register(Colis, ColisAdmin)
