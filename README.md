# Système de Facturation Django

Ce projet est une application web de gestion de produits et de génération de factures, développée avec Django. Elle propose une interface moderne pour la gestion des produits et des factures, la sélection de produits pour les factures, la pagination, et un design esthétique basé sur Bootstrap.

## Fonctionnalités principales
- Gestion CRUD des produits (ajout, modification, suppression, liste, détail)
- Gestion CRUD des factures
- Ajout de produits à une facture
- Pagination des listes
- Interface utilisateur moderne et responsive (Bootstrap + CSS personnalisé)
- Affichage des dates de péremption (ou "Non applicable" si non renseignée)
- Icônes Bootstrap pour une meilleure expérience utilisateur

## Installation

1. **Télécharger le projet**
   ```bash
   cd facturation
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Installer les dépendances**
   ```bash
   pip install django
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collecter les fichiers statiques**
   ```bash
   python manage.py collectstatic
   ```

7. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

8. **Accéder à l'application**
   - Application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Django : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Structure du projet

- `gestion_factures/` : application principale (modèles, vues, formulaires)
- `templates/` : templates HTML (Bootstrap + CSS personnalisé)
- `static/` : fichiers statiques (CSS, images)
- `facturation/` : configuration du projet Django

## Personnalisation
- Le style est basé sur Bootstrap 5 et peut être modifié dans `static/css/style.css`.
- Les icônes sont fournies par [Bootstrap Icons](https://icons.getbootstrap.com/).

## Auteurs
- Réalisé par Mohamed Benasr

## Licence
Ce projet est open-source et libre d'utilisation.
