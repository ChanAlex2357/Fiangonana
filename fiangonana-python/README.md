# Fiangonana

Ce projet consiste a cree une eglise connecter qui sera au profit de ses croyants par le biait des prets sur les "Rakitra"

## Contraintes

- Languages dev : Python ( Gestion des pret )
- Base de donnee : SqlServer
- Affichage : Bureau / Web

## Conception

### Entree

- Dates andatsana rakitra { 52 Alahady }
- Rakitra ( date , montant )
- Info Pret
  - ( date => date actuelle , montant)
  - Mpino manao demande

### Traitement

- connaitre la date de validiter de la caisse
  - alahady farany misy pret

- recuperer la liste des dates 52 pour une annee donnee
  - getAllAlahady( int annee )
  - recuperer les 52 Alahad des 2 dernieres annees

- Recuperer les rakitra

- Calculer le total des montant dans la caisse
  - connaitre la derniere date de pret
  - la date alahady actuelle
  - ? Recuperer par pack de 52 ? totaliter des alhady entre intervalle

- Calculer % augmentation selon donnee
  - Identifier alahady actuelle / farany / misy donnee
  - nombre total jour depuis debut
  - Recuperer donnees correspondant pour annee ( n - 1 )

- Suggrer une date
  - connaitre la date de validiter de la caisse
    - alahady farany misy pret ( caisse = 0)
  - Calcule de estimation
    - Alahady [ id pour annee n ] = Alahady [ id pour annee n-1 ] + %
  - Calculer le total
    - Le reste en caisse + estimation
  - Identifier la date

### Sortie

- Caisse { Montant actuelle }
- Date de pret disponible { date alahady }
