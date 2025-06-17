from django.urls import path
from . import views

urlpatterns = [
    # URLs pour les produits
    path('produits/', views.ProduitListView.as_view(), name='produit-list'),
    path('produits/<int:pk>/', views.ProduitDetailView.as_view(), name='produit-detail'),
    path('produits/nouveau/', views.ProduitCreateView.as_view(), name='produit-create'),
    path('produits/<int:pk>/modifier/', views.ProduitUpdateView.as_view(), name='produit-update'),
    path('produits/<int:pk>/supprimer/', views.ProduitDeleteView.as_view(), name='produit-delete'),
    
    # URLs pour les factures
    path('factures/', views.FactureListView.as_view(), name='facture-list'),
    path('factures/<int:pk>/', views.FactureDetailView.as_view(), name='facture-detail'),
    path('factures/nouvelle/', views.FactureCreateView.as_view(), name='facture-create'),
    path('factures/<int:pk>/modifier/', views.FactureUpdateView.as_view(), name='facture-update'),
    path('factures/<int:pk>/supprimer/', views.FactureDeleteView.as_view(), name='facture-delete'),
    
    # URLs pour les lignes de facture
    path('factures/<int:facture_id>/ajouter-produit/', views.ajouter_produit_facture, name='ajouter-produit'),
    path('lignes/<int:ligne_id>/supprimer/', views.supprimer_produit_facture, name='supprimer-produit'),
    
    # Page d'accueil
    path('', views.ProduitListView.as_view(), name='home'),
]
