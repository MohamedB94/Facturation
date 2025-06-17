from django import forms
from .models import Produit, Facture, LigneFacture

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'date_peremption': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'note']
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

class LigneFactureForm(forms.ModelForm):
    class Meta:
        model = LigneFacture
        fields = ['produit', 'quantite']
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1'})
        }
