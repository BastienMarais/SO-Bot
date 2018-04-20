# Documentation [FR]

## Présentation :

Ce bot a pour but d'automatiser certaines tâches sur le serveur discord du jeu SpaceOrigin.

## Installation :

Pour utiliser ce bot vous avez besoin de :
* python 3.5 ou plus
* la librairie discord.py
* les librairies bs4 et requests
* les fichiers SO-bot.py, joueur.py et secrets.py

Le fichier secrets.py doit être de ce genre :  
```python
#coding: utf-8

ID_BOT = "..."
ID_CHAN_LOG = "..."
ID_CHAN_BOT = "..."
``` 

Une fois les 3 fichiers dans le même répertoire faire :  
```sh
python3.6 SO-bot.py
```

Si tout se passe bien votre shell devrait afficher un message du genre :  
```sh
`Connexion...`
     Logged in as : SO-bot#1722
     ID : 434028726712532992
     Time : `20/04/18  17:52`
```

## Différentes commandes :

Toutes les commandes génèrent un log sur le channel correspondant a l'ID_CHAN_LOG. L'utilisation de ces commandes est limitée au salon correspondant a l'ID_CHAN_BOT sauf pour le staff qui n'est pas limité.

### Pour le staff de SpaceOrigin :

### Pour tout le monde : 
