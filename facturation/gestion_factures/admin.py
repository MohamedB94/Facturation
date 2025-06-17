from django.contrib import admin
from .models import Produit, Facture, LigneFacture

class LigneFactureInline(admin.TabularInline):
    model = LigneFacture
    extra = 1

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'date_peremption')
    search_fields = ('nom',)
    list_filter = ('date_peremption',)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_creation', 'client', 'total', 'nombre_produits')
    inlines = [LigneFactureInline]
    search_fields = ('client',)
    list_filter = ('date_creation',)
