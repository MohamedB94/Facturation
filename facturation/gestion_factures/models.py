from django.db import models
from django.utils import timezone

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField(null=True, blank=True)  # Permettre des valeurs nulles
    
    def __str__(self):
        return self.nom

class Facture(models.Model):
    date_creation = models.DateTimeField(default=timezone.now)
    client = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    
    def __str__(self):
        return f"Facture #{self.id} - {self.date_creation.strftime('%d/%m/%Y')}"
    
    def total(self):
        return sum(ligne.sous_total() for ligne in self.lignes.all())
    
    def nombre_produits(self):
        return sum(ligne.quantite for ligne in self.lignes.all())

class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, related_name='lignes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
    
    def sous_total(self):
        return self.produit.prix * self.quantite
