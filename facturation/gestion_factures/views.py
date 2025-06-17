from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Produit, Facture, LigneFacture
from .forms import ProduitForm, FactureForm, LigneFactureForm

# Vues pour les produits
class ProduitListView(ListView):
    model = Produit
    template_name = 'gestion_factures/produit_list.html'
    context_object_name = 'produits'
    paginate_by = 10

class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'gestion_factures/produit_detail.html'
    context_object_name = 'produit'

class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'gestion_factures/produit_form.html'
    success_url = reverse_lazy('produit-list')

    def form_valid(self, form):
        messages.success(self.request, 'Produit créé avec succès.')
        return super().form_valid(form)

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'gestion_factures/produit_form.html'
    success_url = reverse_lazy('produit-list')

    def form_valid(self, form):
        messages.success(self.request, 'Produit mis à jour avec succès.')
        return super().form_valid(form)

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'gestion_factures/produit_confirm_delete.html'
    success_url = reverse_lazy('produit-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Produit supprimé avec succès.')
        return super().delete(request, *args, **kwargs)

# Vues pour les factures
class FactureListView(ListView):
    model = Facture
    template_name = 'gestion_factures/facture_list.html'
    context_object_name = 'factures'
    paginate_by = 10

class FactureDetailView(DetailView):
    model = Facture
    template_name = 'gestion_factures/facture_detail.html'
    context_object_name = 'facture'

class FactureCreateView(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'gestion_factures/facture_form.html'
    success_url = reverse_lazy('facture-list')

    def form_valid(self, form):
        messages.success(self.request, 'Facture créée avec succès.')
        return super().form_valid(form)

class FactureUpdateView(UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'gestion_factures/facture_form.html'
    success_url = reverse_lazy('facture-list')

    def form_valid(self, form):
        messages.success(self.request, 'Facture mise à jour avec succès.')
        return super().form_valid(form)

class FactureDeleteView(DeleteView):
    model = Facture
    template_name = 'gestion_factures/facture_confirm_delete.html'
    success_url = reverse_lazy('facture-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Facture supprimée avec succès.')
        return super().delete(request, *args, **kwargs)

# Vue pour ajouter des produits à une facture
def ajouter_produit_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    
    if request.method == 'POST':
        form = LigneFactureForm(request.POST)
        if form.is_valid():
            ligne = form.save(commit=False)
            ligne.facture = facture
            ligne.save()
            messages.success(request, 'Produit ajouté à la facture avec succès.')
            return redirect('facture-detail', pk=facture.id)
    else:
        form = LigneFactureForm()
    
    return render(request, 'gestion_factures/ajouter_produit.html', {
        'form': form,
        'facture': facture
    })

# Vue pour supprimer un produit d'une facture
def supprimer_produit_facture(request, ligne_id):
    ligne = get_object_or_404(LigneFacture, id=ligne_id)
    facture_id = ligne.facture.id
    ligne.delete()
    messages.success(request, 'Produit retiré de la facture avec succès.')
    return redirect('facture-detail', pk=facture_id)
