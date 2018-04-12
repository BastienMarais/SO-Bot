#coding: utf-8
#########################################################################################
#   Description :   Ce programme gère le bot discord du même nom
#   File :          SO-bot.py
#   Usage :         python3 SO-bot.py
#   Requirements :  python3.7 and discord.py
#   User.name :     Bastien Marais
#   User.email :    marais.bas@gmail.com                        
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
    """ [MESSAGE] fait écrire votre message par le bot """
    
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
    """ []  affiche son profil discord sur le serveur """
    
    print(log_str("COMMANDE",ctx.message))
    await bot.say(me_str(ctx.message))

        

@bot.command(pass_context = True)
async def aff(ctx ,*, message : str):
    """ [PSEUDO]  affiche le profil SpaceOrigin du joueur passé en paramètre """
 
    print(log_str("COMMANDE",ctx.message))
    await bot.say("http://bigbang.spaceorigin.fr/profile/"+message)

            

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
    if message.content.startswith("!"):
        log_type = "COMMANDE"
    
    # si c'est un message 
    if log_type == "MESSAGE":
        log = "| " + log_type + " | " + str(message.channel) + " | " + str(message.author) + " : " + message.content
        
    # si c'est une commande
    elif log_type == "COMMANDE" :
        log = str(message.timestamp) + " | " + str(message.author) + " | " + log_type + " | " + message.content 
    
    # renvoie le log formaté
    return log
    
    
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

