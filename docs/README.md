# Documentation [FR]

Ce bot a pour but d'automatiser certaines tâches sur le serveur discord du jeu SpaceOrigin.


## Installation :

Pour utiliser ce bot vous avez besoin de :
* python 3.5 ou plus
* la librairie discord.py
* les librairies bs4 et requests
* les fichiers SO-bot.py, joueur.py, originel.py et secrets.py

Le fichier secrets.py doit être de ce genre :  
```python
#coding: utf-8

ID_BOT = "..."
ID_CHAN_LOG = "..."
ID_CHAN_BOT = "..."
``` 

Une fois les 4 fichiers dans le même répertoire faire :  
```sh
python3.6 SO-bot.py
```

Si tout se passe bien votre shell devrait afficher un message du genre :  
```
Connexion...
     Logged in as : SO-bot#1722
     ID : 434028726712532992
     Time : 20/04/18  17:52
```

## Différentes commandes :

Toutes les commandes génèrent un log sur le channel correspondant a l'ID_CHAN_LOG. L'utilisation de ces commandes est limitée au salon correspondant a l'ID_CHAN_BOT sauf pour le staff qui n'est pas limité. Toutes les commandes s'activent avec "!".

### Pour le staff de SpaceOrigin :

#### 1) La commande !say

Permet de faire parler le bot.  
Elle prend en paramètre le message qu'on veut lui faire dire.

#### 2) La commande !mute 

Permet de mute un membre du serveur.  
Elle prend en paramètre seulement la mention du membre.

#### 3) La commande !demute

Permet de demute un membre du serveur.  
Elle prend en paramètre seulement la mention du membre.

#### 4) La commande !roles 

Permet d'attribuer un pack de rôles a un membre du serveur.  
Elle prend en paramètre la mention du membre, son statut et sa planète.

Statut : citoyen / gouv / empereur.  
Planète : le nom d'une des 11 planètes en minuscule et sans accents.

#### 5) La commande !ori

Permet d'écrire le message donné en mode originel.  
Elle prend en paramètre le message.

#### 6) La commande !trad

Permet de tranformer un message originel, séparé lettre par lettre.  
Prend en paramètre le message.

### Pour tout le monde : 

#### 1) La commande !me

Permet d'afficher son profil discord.  
Elle ne prend pas de paramètre.

#### 2) La commande !profil 

Permet d'afficher le profil d'un joueur de SpaceOrigin.  
Elle prend en paramètre seulement le pseudo du joueur.

#### 3) La commande !rand

Permet de générer des nombres aléatoires.  
Elle prend en paramètre le nombre de tirages, le minimum et maximum.

#### 4) La commande !pub  

Permet d'afficher les liens utiles du jeu SpaceOrigin.  
Elle ne prend pas de paramètre.

### TODO :

* Un jeu du pendu avec pour thématique SpaceOrigin
* J'ai pas plus d'inspiration pour le moment ^^


