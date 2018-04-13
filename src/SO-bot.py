#coding: utf-8
#########################################################################################
#   Description :   Ce programme gère le bot discord du même nom
#   File :          SO-bot.py
#   Usage :         python3 SO-bot.py
#   Requirements :  python3.7 and discord.py
#   User.name :     Bastien Marais
#   User.email :    marais.bas@gmail.com                        
#   Trucs utiles :  https://cog-creators.github.io/discord-embed-sandbox/
#########################################################################################


"""
#########################################################################################
#                            Différents imports                                      
#########################################################################################
"""

import discord
import asyncio
from discord.ext.commands import Bot

# contient ID_BOT
import secrets

# initialisation du bot
bot = Bot(command_prefix="!") 

"""
#########################################################################################
#                            Fonctions d'events                                      
#########################################################################################
"""

@bot.event
async def on_ready():
    """ s'éxécute quand le bot est connecté et opérationnel """
    name = bot.user.display_name + "#" + bot.user.discriminator
    print("Logged in as : ",name)
    print("ID : ", bot.user.id)
        
 
"""
#########################################################################################
#                            Différentes commandes                                     
#########################################################################################
"""

@bot.command(pass_context = True)
async def say(ctx ,*, message : str) :
    """ [MESSAGE] Ecrit votre message par le bot, réservé au staff. """
    
    # si c'est un membre du staff voulant le faire
    if check_staff(ctx.message):
        msg = message
        await bot.delete_message(ctx.message)
        
    # sinon
    else :
        msg = "Vous n'êtes pas autorisé à jouer avec cette commande"

    print(log_str("COMMANDE",ctx.message))
    await bot.say(msg)


    
@bot.command(pass_context = True)
async def me(ctx ,*args) : 
    """ []  Affiche son profil discord sur le serveur. """
    
    print(log_str("COMMANDE",ctx.message))
    await bot.say(me_str(ctx.message))

        

@bot.command(pass_context = True)
async def profil(ctx ,*, message : str):
    """ [JOUEURS] Affiche le profil SpaceOrigin des JOUEURS, séparer par ' '. """
 
    print(log_str("COMMANDE",ctx.message))
    await bot.say(profil_str(message))

@bot.command(pass_context = True)
async def pub(ctx, *args):
    """ [] Fait de la pub pour SpaceOrigin. """

    print(log_str("COMMANDE",ctx.message))
    await bot.say(pub_str())



"""
#########################################################################################
#                            Différentes fonctions                                   
#########################################################################################
"""


def me_str(message):
    """ renvoie la string correspondant a la commande !me """
  
    # initialisation
    membre = message.author
    roles = []
    
    # on transforme chacun des rôles en str
    for r in membre.roles : 
        roles.append(str(r))
    # on retire everyone 
    roles.remove("@everyone") 
                
    # mise en forme du texte a afficher
    texte = "```md\n"
    texte += "# Pseudo : " + membre.display_name + "\n"
    texte += "Rôle(s) : " + str(roles) + "\n"
    texte += "Date d'arrivée : " + str(membre.joined_at) + "\n"
    texte += "```"
    
    # renvoie le texte 
    return texte

def log_str(log_type,message):
    """ renvoie la string du log console formatée """
    
    # initialisation
    log = ""
        
    # si c'est une commande
    if log_type == "COMMANDE" :
        log =  log_type + " | " + str(message.timestamp) + " | " + str(message.author) + " | " + message.content 
    
    # renvoie le log formaté
    return log

def pub_str():
    """ renvoie la string correspondant à la commande !pub """

    # initialisations
    texte = ""    
    URL_JEU = "https://play.spaceorigin.fr/"
    URL_BOUTIQUE = ""
    URL_TCHAT = ""
    URL_FORUM = ""
    URL_DISCORD = ""
    EVENT = "Concours CBEE : Restaurations des Données [En cours]"
    URL_VOTE = ["","",""]


    # mise en forme
    texte += "```md\n##########\n# PUB\n##########\n\n"
    texte += "# Jeu :\n* " + URL_JEU + "\n"
    texte += "# Shop :\n* " + URL_BOUTIQUE + "\n\n"

    texte += "# Jeu :\n* " + URL_TCHAT + "\n"
    texte += "# Forum :\n* " + URL_FORUM + "\n"
    texte += "# Discord :\n* " + URL_DISCORD + "\n\n"

    if EVENT != "" :
        texte += "# Event :\n" + EVENT + "\n\n"

    texte += "# Voter pour Spaceorigin sur :\n"
    for url in URL_VOTE :
        texte += "* " + url + "\n"

    texte += "\n##########\n# PUB\n##########\n```"

    # renvoie le texte formaté
    return texte
    

def profil_str(message):
    """ renvoie la string correspondant à la commande !profil """

    # initialisations 
    texte = ""
    args = message.split(" ")
    URL = "http://bigbang.spaceorigin.fr/profile/"

    # mise en forme
    for j in args :
        texte += URL + j +"\n" 

    # renvoie la string formatée
    return texte

"""
#########################################################################################
#                                Fonctions de check                                     
#########################################################################################
"""

def check_staff(message):
    """ renvoie True si l'auteur est un membre du staff sinon False """
    membre = message.author 
    roles = []
    for r in membre.roles :
        roles.append(str(r))
        
    for role in roles :
        if role == "staff":
            return True
    return False
   
   
"""
#########################################################################################
#                                       Main                                     
#########################################################################################
""" 

bot.run(secrets.ID_BOT)

