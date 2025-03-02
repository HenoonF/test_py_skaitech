# Test Technique: SkAI Tech Crew Management System

## Contexte
Vous travaillez pour une compagnie aérienne qui doit gérer la disponibilité et les contrats de son personnel navigant. Le système actuel doit être amélioré et modernisé avec une API REST.

## Spécifications

### Règles métier
Chaque membre d'équipage a un contrat avec la compagnie aérienne avec les attributs suivants: 
- `id` (int): identifiant unique
- `name` (string): nom du membre d'équipage
- `role` (string): rôle du membre d'équipage (PILOT, CABIN_CREW, GROUND_STAFF, INSTRUCTOR)
- `contract_days` (int): nombre de jours de contrat restants
- `availability` (int): nombre de jours de disponibilité restants

### Les règles de gestion des disponibilités
- La disponibilité diminue chaque jour basé sur certaines règles:
    - Les pilotes perdent 1 jour de disponibilité par jour
    - Le personnel de cabine perd 1.5 jours par jour
    - L'équipe au sol perd 0.5 jour par jour
- Si le membre d'équipage a moins de 5 jours de disponibilité, il doit être mis en repos
- Un membre ne peut pas avoir plus de jours de disponibilité que son contrat
- La disponibilité ne peut pas être négative
- Certains rôles spéciaux (instructeurs) ne perdent pas de disponibilité.

## Mission
1. Créer une API REST avec FastAPI qui permet de:

Certaines des routes ont déjà été implémentées dans `main.py`: ta mission sera de les compléter si besoin et d'ajouter la logique des routes manquantes (marquées par un commentaire `# TODO`).

- Lister tous les membres d'équipage
- Ajouter un nouveau membre d'équipage
- Supprimer un membre d'équipage
- Mettre à jour la disponibilité
- Obtenir les statistiques de disponibilité par rôle au format suivant ["ROLE": {"total": 0, "available": 0},] avec total le nombre de membres d'équipage par rôle et available le nombre de membres d'équipage disponibles (pas en repos à l'instant t)

2. Implémenter la logique de mise à jour quotidienne des disponibilités définis dans les spécifications


## Contraintes
- Utiliser FastAPI
- Ne pas modifier CrewMember
- Ne pas modifier les noms et chemin des routes API
- Tu pourras librement modifier les fichiers `main.py`, `schema.py` et `service.py` 

## Remarques
Pour simplifier le problème, les données ne sont pas stocké en base de donnée, mais dans le script python directement. A chaque modification de la codebase, les données sont réinitialisées aux données d'origine.


## Critères d'évaluation
- Qualité et organisation du code
- Respect des règles métiers
- Gestion des erreurs
- Documentation

# Utilisation de la codebase
- Créer un environnement virtuel venv avec python > 3.12 (`python -m venv venv`)
- Activer l'environnement virtuel (`source venv/bin/activate` sur mac/linux, `venv\Scripts\activate` sur windows)
- Installer les dépendances avec `pip install -r requirements.txt`
- Lancer le serveur avec `uvicorn app.main:app --reload`

# Documentation
Voici la liste des modifications effectuées : 

## Dans `schema`
Ajout de l'id dans CrewMemberResponse pour avoir l'id dans la liste d'équipage, ce qui est plus pratique.

## Dans `service`
Implémentation de la logique de mise à jour quotidienne de la disponibilité (entre autres). Il m'a manqué quelques éléments potentiels, comme la manière dont mettre un employé au repos ou le choix ou non de supprimer des membres en fin de contrat.

## Dans `main`
Implémantation des routes demandées. Modification de `post`. Ajout de quelques fonctions auxiliares comme `get_next_id`
