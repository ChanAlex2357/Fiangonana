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

- Info Pret ( date => date actuelle , montant)

### Traitement

- recuperer la liste des dates 52 pour une annee donnee
  - getAllAlahady( int annee )

### Sortie

- Caisse { Montant actuelle }
- Date de pret disponible { date alahady }
