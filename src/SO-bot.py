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
import time 

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
    
    # initialisation
    texte = "`Connexion...`\n"
    name = bot.user.name + "#" + bot.user.discriminator
    
    # mise en forme
    texte += "     Logged in as : " + name + "\n"
    texte += "     ID : " + bot.user.id + "\n"
    texte += "     Time : " + getTime()
    
    # génération d'un log console
    print(texte)
    
    # génération d'un log sur bot-logs
    channel = discord.Object("434349278283038760")
    await bot.send_message(channel,texte)
        
@bot.event
async def on_member_join(member):
    """ s'éxécute quand quelqu'un rejoint le serveur """
    
    # initialisation
    texte = welcome_str()
    
    # envoi un message au nouveau membre
    await bot.send_message(member,texte)
    
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

    # génération d'un log sur bot-logs
    await log(ctx)
    await bot.say(msg)


    
@bot.command(pass_context = True)
async def me(ctx ,*args) : 
    """ []  Affiche son profil discord sur le serveur. """
    
    # génération d'un log sur bot-logs
    await log(ctx)
    
    # envoie le message sur le même channel
    await bot.say(me_str(ctx.message))

        

@bot.command(pass_context = True)
async def profil(ctx ,*, message : str):
    """ [JOUEURS] Affiche le profil SpaceOrigin des JOUEURS, séparer par ' '. """

    # génération d'un log sur bot-logs
    await log(ctx)
    
    # envoie le message sur le même channel    
    await bot.say(profil_str(message))

@bot.command(pass_context = True)
async def pub(ctx, *args):
    """ [] Fait de la pub pour SpaceOrigin. """

    # génération d'un log sur bot-logs
    await log(ctx)
    
    # envoie le message sur le même channel
    await bot.say(pub_str())


@bot.command(pass_context = True)
async def mute(ctx ,*, message : str) :
    """ [JOUEUR] [INT] [h/j] """
    
    # initialisation 
    msg = ""
    
    # si c'est un membre du staff voulant le faire
    if check_staff(ctx.message):
    
        msg = mute_str(ctx)
        await bot.delete_message(ctx.message)
        
    # sinon
    else :
        msg = "Vous n'êtes pas autorisé à jouer avec cette commande"

    # génération d'un log sur bot-logs
    await log(ctx)
    
    # envoie le message sur le même channel
    await bot.say(msg)
    
    


"""
#########################################################################################
#                            Fonctions d'affichage                                   
#########################################################################################
"""

def mute_str(ctx):
    """ renvoie la string d'affichage de !mute """
    
    # initialisation
    texte = ""
    cible_val = ""
    args = ctx.message.content.split(" ")
    URL_GIF = "https://78.media.tumblr.com/tumblr_lrh786mY3U1qlwcbao1_500.gif"
  
    # on récupère le membre et son nom
    m = get_membre(ctx.message,args[1])  
    cible_val = m.name + "#" + m.discriminator 
            
    # on récupère la durée et l'unité ( h / j ) 
    duree_val = str(args[2])
    duree_val += str(args[3])
    
    # mise en forme
    texte += "```md\n# MUTE\n"
    texte += "Cible : " + cible_val + "\nDurée : " + duree_val + "\n```"
    texte += "\n" + URL_GIF + "\n"
       
    # renvoie la chaine formatée
    return texte
    

def welcome_str():
    """ renvoie la string du message d'accueil """
    
    # initialisation
    texte = ""
    
    # mise en forme 
    texte += "Bonjour et bienvenue sur SO Officiel !\n"
    texte += "Passez sur le salon demandes d\'accès pour obtenir vos rôles.\n"
    texte += "Regardez le message épinglé de ce salon tout est expliqué."
    
    return texte
    
def me_str(message):
    """ renvoie la string correspondant a la commande !me """
  
    # initialisation
    membre = message.author
    roles = []
    t = str(membre.joined_at.strftime("%d/%m/%y  %H:%M"))
    
    # on transforme chacun des rôles en str
    for r in membre.roles : 
        roles.append(str(r))
        
    # on retire everyone 
    roles.remove("@everyone") 
                
    # mise en forme du texte a afficher
    texte = "```md\n"
    texte += "# Pseudo : " + membre.display_name + "\n"
    texte += "Rôle(s) : " + str(roles) + "\n"
    texte += "Date d'arrivée : " + str(t) + "\n"
    texte += "```"
    
    # renvoie le texte 
    return texte

def pub_str():
    """ renvoie la string correspondant à la commande !pub """

    # initialisations
    texte = ""    
    URL_JEU = "https://play.spaceorigin.fr/"
    URL_SUPPORT = "http://support.spaceorigin.fr/"
    URL_BOUTIQUE = "http://shop.spaceorigin.fr/"
    URL_TCHAT = "http://bigbang.spaceorigin.fr/chat.php"
    URL_FORUM = "https://forum.spaceorigin.fr/"
    URL_DISCORD = "https://discord.gg/ejnnxtB"
    URL_FACEBOOK = "https://www.facebook.com/SpaceOriginFr/"
    EVENT = "Concours CBEE : Restaurations des Données [En cours]"
    URL_VOTE = []
    URL_VOTE.append("http://www.jeux-alternatifs.com/SpaceOrigin-jeu647_hit-parade_1_1.html")
    URL_VOTE.append("https://www.mmorpg.fr/classement/space-origin.html")

    # mise en forme
    texte += "```md\n##########\n# PUB\n##########\n\n"
    texte += "# Jeu :\n* " + URL_JEU + "\n"
    texte += "# Support :\n* " + URL_SUPPORT + "\n"
    texte += "# Shop :\n* " + URL_BOUTIQUE + "\n\n"

    texte += "# Tchat :\n* " + URL_TCHAT + "\n"
    texte += "# Forum :\n* " + URL_FORUM + "\n"
    texte += "# Discord :\n* " + URL_DISCORD + "\n"
    texte += "# Facebook :\n* " + URL_FACEBOOK + "\n"

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
#                                Fonctions de logs                                     
#########################################################################################
"""

async def log(ctx):
    """ redirige les logs commandes vers le salon bot-logs """
    
    channel = discord.utils.get(ctx.message.server.channels, name="bot-logs")
    await bot.send_message(channel,log_str(ctx.message))
    
    
def log_str(message):
    """ renvoie la string du log console formatée """
    
    # initialisation
    log = ""
        
    log = getTime() + "  |  "  + str(message.channel) + "  |  " + str(message.author) + " :\n     " + message.content 
    
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
   
def check_roles(message,membre_id,liste_roles):
    """ renvoie True si l'utilisateur avec l'id donné, a la liste de rôles donnée """
    
    # initialisation
    membre = ""
    roles = []
    nb_roles = 0
    nb_liste_roles = 0
    nb_valide = 0
    
    # on récupère notre membre
    membre = get_membre(message,membre_id)
    
    # on récupère les rôles
    roles = get_roles(message,membre)
        
    # on calcule le nombre de rôles de chaque liste
    nb_roles = len(roles)
    nb_liste_roles = len(liste_roles)
    
    # s'il a moins de rôles que ceux demandés
    if nb_roles < nb_liste_roles :
        return False
        
    # s'il en a autant ou plus
    else :
    
        # on regarde chacun des rôles
        for role in roles :
        
            if role in liste_roles:
                nb_valide += 1
        
        # si a la fin on a tous les rôles  
        if nb_valide == nb_liste_roles :
            return True
        
        # s'il n'a pas les rôles demandés
        else :
            return False
        
    
"""
#########################################################################################
#                                Fonctions utilitaires                                     
#########################################################################################
"""

def getTime():
    """ renvoie la str de l'heure actuelle """
    
    return str("`" + time.strftime("%d/%m/%y  %H:%M",time.localtime()) + "`")


def get_membre(message, membre_id):
    """ renvoie un objet de type membre correspondant a la recherche """
    
    # on regarde tous les membres du serveur
    for m in message.server.members :
        courant_name = str("<@" + m.id + ">")
        courant_name2 = str("<@!" + m.id + ">")
        
        # si on a trouvé le joueur mentionné
        if courant_name == membre_id or courant_name2 == membre_id:
            return m
            
def get_roles(message,membre):
    """ renvoie la liste des rôles du membre donné sous forme de str """
    
    # initialisation
    roles = []
    
    # On regarde tous les rôles qu'il a 
    for r in membre.roles :
        roles.append(str(r))
        
    # renvoie la liste des rôles sous forme de liste de str
    return roles
    
"""
#########################################################################################
#                                       Main                                     
#########################################################################################
""" 

bot.run(secrets.ID_BOT)

