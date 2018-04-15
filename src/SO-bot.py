#coding: utf-8
#########################################################################################
#   Description :   Ce programme gère le bot discord du même nom
#   File :          SO-bot.py
#   Usage :         python3 SO-bot.py
#   Requirements :  python3 and discord.py
#   User.name :     Bastien Marais
#   User.email :    marais.bas@gmail.com                        
#   Ressources :    https://cog-creators.github.io/discord-embed-sandbox/
#                   http://discordpy.readthedocs.io/en/latest/api.html
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
from joueur import * 

# contient ID_BOT
import secrets

# initialisation du bot
bot = Bot(command_prefix="!") 

URL_WAIT = "https://media.giphy.com/media/i9pILLyvafPkk/giphy.gif"
URL_MUTE = "https://78.media.tumblr.com/tumblr_lrh786mY3U1qlwcbao1_500.gif"
URL_KING = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf01.png"
URL_ASSISTANT = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf02.png"
URL_MOD_FORUM = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf03.png"
URL_ANIM = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf04.png"
URL_MOD_JEU = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf05.png"
URL_ADMIN = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf06.png"
RED = discord.Colour(7014674)
GREEN = discord.Colour(3445292)
BLUE = discord.Colour(3052451)


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
    await bot.say(embed=me_emb(ctx.message))

        
@bot.command(pass_context = True)
async def profil(ctx ,*, message : str):
    """ [JOUEURS] Affiche le profil SpaceOrigin des JOUEURS, séparer par ' '. """

    # génération d'un log sur bot-logs
    await log(ctx)
    
    # texte du message d'attente
    texte = "`Veuillez patienter...`\n" + URL_WAIT
    
    # envoie la réponse et le message d'attente sur le même channel
    my_message = await bot.send_message(ctx.message.channel,texte)
    await bot.say(profil_str(message))
    await bot.delete_message(my_message)


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
    
        msg = mute_emb(ctx)
        await bot.delete_message(ctx.message)
        
        # envoie le message sur le même channel
        await bot.say(embed=msg)
        
    # sinon
    else :
        msg = "Vous n'êtes pas autorisé à jouer avec cette commande"
        
        # envoie le message sur le même channel
        await bot.say(msg)
        
    # génération d'un log sur bot-logs
    await log(ctx)
    
    
    
"""
#########################################################################################
#                            Fonctions d'affichage                                   
#########################################################################################
"""


def mute_emb(ctx):
    """ renvoie le embed de !mute """
    
    # initialisation
    cible_val = ""
    args = ctx.message.content.split(" ")
    embed = discord.Embed(title="`Un MUTE est tombé !`", colour=RED, url="", description="")
    embed.set_image(url=URL_MUTE)
    embed.set_thumbnail(url=URL_ADMIN)
    embed.set_author(name="SO-Tribunal", url="", icon_url=URL_ADMIN)
    embed.set_footer(text="A la prochaine ;-)", icon_url="")
  
    # on récupère le membre et son nom
    m = get_membre(ctx.message,args[1])  
    cible_val = m.name + "#" + m.discriminator 
            
    # on récupère la durée et l'unité ( h / j ) 
    duree_val = str(args[2])
    duree_val += str(args[3])

    embed.add_field(name="Cible : ", value=cible_val,inline=True)
    embed.add_field(name="Durée : ", value=duree_val,inline=True)

    # renvoie l'embed correspondant
    return embed


def welcome_str():
    """ renvoie la string du message d'accueil """
    
    # initialisation
    texte = ""
    
    # mise en forme 
    texte += "Bonjour et bienvenue sur SO Officiel !\n"
    texte += "Passez sur le salon demandes d\'accès pour obtenir vos rôles.\n"
    texte += "Regardez le message épinglé de ce salon tout est expliqué."
    
    return texte
    
    
def me_emb(message):
    """ renvoie la string correspondant a la commande !me """
  
    # initialisation
    membre = message.author
    roles = []
    t = str(membre.joined_at.strftime("%d/%m/%y  %H:%M"))
    embed = discord.Embed(title="`Votre profil discord`", colour=BLUE, url="", description="")
    embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
    embed.set_thumbnail(url=URL_MOD_FORUM)
    embed.set_footer(text="Heureux de vous avoir aidé ;-)", icon_url="")
    
    # on transforme chacun des rôles en str
    roles = get_roles(message,membre)
                
    # mise en forme du embed a afficher
    embed.add_field(name="Pseudo : ", value=membre.display_name,inline=True)
    embed.add_field(name="Date d'arrivée : ", value=str(t),inline=True)
    embed.add_field(name="Rôles : ", value=str(roles),inline=False)
    
    
    # renvoie l'embed 
    return embed


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
    texte += "# Facebook :\n* " + URL_FACEBOOK + "\n\n"

    if EVENT != "" :
        texte += "# Event :\n* " + EVENT + "\n\n"

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

    # mise en forme
    for j in args :
        texte += str(Joueur(j)) + "\n"

    # renvoie la string formatée
    return texte


"""
#########################################################################################
#                                Fonctions de logs                                     
#########################################################################################
"""


async def log(ctx):
    """ redirige les logs commandes vers le salon bot-logs """
    
    # récupère le channel où il faut envoyer les logs
    channel = discord.utils.get(ctx.message.server.channels, name="bot-logs")
    
    # envoie le log
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
    
    # initialisation
    membre = message.author 
    
    # renvoie le résultat du test des rôles
    return check_roles(message,membre,["staff"])
 
   
def check_roles(message,membre,liste_roles):
    """ renvoie True si l'utilisateur avec l'id donné, a la liste de rôles donnée """
    
    # initialisation
    roles = []
    nb_roles = 0
    nb_liste_roles = 0
    nb_valide = 0
    
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
        
    # on retire everyone 
    roles.remove("@everyone") 
    
    # renvoie la liste des rôles sous forme de liste de str
    return roles
    
    
"""
#########################################################################################
#                                       Main                                     
#########################################################################################
""" 

bot.run(secrets.ID_BOT)


