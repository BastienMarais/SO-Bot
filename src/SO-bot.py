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
from random import *
from originel import *

# contient ID_BOT, ID_CHAN_BOT et ID_CHAN_LOG
import secrets

# initialisation du bot
bot = Bot(command_prefix="!") 

URL_WAIT = "https://media.giphy.com/media/i9pILLyvafPkk/giphy.gif"
URL_WAIT2 = "https://media.giphy.com/media/Ml1xQjpBncN4k/giphy.gif"
URLS_WAIT = [URL_WAIT,URL_WAIT2]
URL_RAND = "https://media.giphy.com/media/ldSHPxXrtL8Yw/giphy.gif"
URL_DEMUTE = "https://media.giphy.com/media/LtlYX81u51Uys/giphy.gif"
URL_MUTE = "https://78.media.tumblr.com/tumblr_lrh786mY3U1qlwcbao1_500.gif"
URL_KING = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf01.png"
URL_ASSISTANT = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf02.png"
URL_MOD_FORUM = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf03.png"
URL_ANIM = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf04.png"
URL_MOD_JEU = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf05.png"
URL_ADMIN = "http://image.noelshack.com/fichiers/2018/15/7/1523794762-avatar-staf06.png"
RED = discord.Colour(7014674) # en cas de sanction et erreur
GREEN = discord.Colour(3445292) # en cas de succès ou récompense
BLUE = discord.Colour(3052451) # en cas d'affichage d'information
YELLOW = discord.Colour(9597740) # en cas de pub


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
    channel = discord.Object(secrets.ID_CHAN_LOG)
    await bot.send_message(channel,texte)
        
        
@bot.event
async def on_member_join(member):
    """ s'éxécute quand quelqu'un rejoint le serveur """
    
    # initialisation
    texte = welcome_emb()
    
    # envoi un message au nouveau membre
    await bot.send_message(member,embed = texte)
    
    
"""
#########################################################################################
#                            Différentes commandes STAFF                                     
#########################################################################################
"""


@bot.command(pass_context = True)
async def say(ctx ,*, message : str) :
    """ [MESSAGE] Ecrit votre message par le bot, réservé au staff. """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
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
async def ori(ctx ,*, message : str) :
    """ [MESSAGE] Ecrit votre message en mode originel, réservé au staff. """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # si c'est un membre du staff voulant le faire
        if check_staff(ctx.message):
            o = Originel()
            msg = o.toOriginel(message)
            
        # sinon
        else :
            msg = "Vous n'êtes pas autorisé à jouer avec cette commande"

        # génération d'un log sur bot-logs
        await log(ctx)
        await bot.say(msg)
        

@bot.command(pass_context = True)
async def trad(ctx ,*, message : str) :
    """ [MESSAGE] Traduit votre message originel, réservé au staff. """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # si c'est un membre du staff voulant le faire
        if check_staff(ctx.message):
            o = Originel()
            msg = o.toNormal(message)
            
        # sinon
        else :
            msg = "Vous n'êtes pas autorisé à jouer avec cette commande"

        # génération d'un log sur bot-logs
        await log(ctx)
        await bot.say(msg)


@bot.command(pass_context = True)
async def mute(ctx ,*, message : str) :
    """ [JOUEUR] Mute le joueur """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # initialisation     
        msg = ""
        
        # si c'est un membre du staff voulant le faire
        if check_staff(ctx.message):
        
            # initialisation 
            msg = mute_emb(ctx)
            roles = {}
            for r in ctx.message.server.roles :
                roles[r.name] = r
            membre = ctx.message.mentions[0]
                
            await bot.delete_message(ctx.message)
            await bot.replace_roles(membre,roles["MUTE"])
            
            # envoie le message sur le même channel
            await bot.say(embed=msg)
            
        # sinon
        else :
            
            # envoie le message sur le même channel
            msg = "Vous n'êtes pas autorisé à jouer avec cette commande"
            await bot.say(msg)
            
        # génération d'un log sur bot-logs
        await log(ctx)
    
    
@bot.command(pass_context = True)
async def demute(ctx ,*, message : str) :
    """ [JOUEUR] Démute le joueur """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # initialisation     
        msg = ""
        
        # si c'est un membre du staff voulant le faire
        if check_staff(ctx.message):
        
            # initialisation 
            msg = demute_emb(ctx)
            roles = {}
            for r in ctx.message.server.roles :
                roles[r.name] = r
            membre = ctx.message.mentions[0]
                
            await bot.delete_message(ctx.message)
            await bot.remove_roles(membre,roles["MUTE"])
            
            # envoie le message sur le même channel
            await bot.say(embed=msg)
            
        # sinon
        else :
            
            # envoie le message sur le même channel
            msg = "Vous n'êtes pas autorisé à jouer avec cette commande"
            await bot.say(msg)
            
        # génération d'un log sur bot-logs
        await log(ctx)


@bot.command(pass_context = True)
async def roles(ctx ,*, message : str) :
    """ [JOUEUR] [citoyen/gouv/empereur] [Planète] """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # initialisation     
        msg = ""
        
        # si c'est un membre du staff voulant le faire
        if check_staff(ctx.message):
        
            # initialisation 
            membre = ctx.message.mentions[0]
            planete = message.split(" ")[2]
            statut = message.split(" ")[1] 
            membre_roles = get_roles(message,membre)
            roles = {}
            alliance = ""
            for r in ctx.message.server.roles :
                roles[r.name] = r
                
            # on regarde si le joueur a une alliance
            for m_r in membre_roles :
                if m_r.startswith("alliance") :
                    alliance = m_r
            
            # on attribut le pack de rôles correspondant
            if statut == "citoyen" :
                cle = "citoyen" + "-" + planete
                if alliance != "" :
                    await bot.replace_roles(membre,roles[cle],roles[alliance])
                else :
                    await bot.replace_roles(membre,roles[cle])
                    
            elif statut == "gouv" :
                cle1 = "citoyen" + "-" + planete
                cle2 = "gouv" + "-" + planete
                if alliance != "" :
                    await bot.replace_roles(membre,roles[cle1], roles[cle2], roles[alliance])
                else :
                    await bot.replace_roles(membre,roles[cle1], roles[cle2])  
                
            elif statut == "empereur" :
                cle1 = "citoyen" + "-" + planete
                cle2 = "gouv" + "-" + planete
                cle3 = "empereur" + "-" + planete
                if alliance != "" :
                    await bot.replace_roles(membre,roles[cle1], roles[cle2], roles[cle3], roles[alliance])
                else :
                    await bot.replace_roles(membre,roles[cle1], roles[cle2], roles[cle3])
            else :
                await bot.say("Tu t'es encore fail Billy ! Recommences, ça ne coute rien ;)")
                return
                
            await bot.delete_message(ctx.message)
            
            # envoie le message sur le même channel
            msg = roles_emb(ctx,membre,planete,statut)
            await bot.say(embed = msg)
            
        # sinon
        else :
            
            # envoie le message sur le même channel
            msg = "Vous n'êtes pas autorisé à jouer avec cette commande"
            await bot.say(msg)
            
        # génération d'un log sur bot-logs
        await log(ctx)
    
        
"""
#########################################################################################
#                            Différentes commandes ALL                                     
#########################################################################################
"""   


@bot.command(pass_context = True)
async def rand(ctx ,*, message : str):
    """ [NB_ESSAIS] [MIN] [MAX] renvoie le(s) nombre(s) aléatoire(s) demandé(s) """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # génération de log
        await log(ctx) 
        
        # initialisation
        limite_essais = 100
        limite_max = 1000
        limite_min = -1000
        nb_essais = int(message.split(" ")[0])
        mini = int(message.split(" ")[1])
        maxi = int(message.split(" ")[2])
        liste_nb = []
        
        # on check les limites 
        if maxi > limite_max :
            maxi = limite_max
        if mini < limite_min :
            mini = limite_min
        if nb_essais > limite_essais :
            nb_essais = limite_essais
        
        # on fait les tirages
        for i in range(nb_essais):
            liste_nb.append(randint(mini,maxi))
        liste_nb.sort()
        
        # affiche le résultat
        await bot.say(embed = rand_emb(liste_nb,mini,maxi,nb_essais))
    
    
@bot.command(pass_context = True)
async def me(ctx ,*args) : 
    """ []  Affiche son profil discord sur le serveur """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # génération d'un log sur bot-logs
        await log(ctx)
        
        # envoie le message sur le même channel
        await bot.say(embed=me_emb(ctx))

        
@bot.command(pass_context = True)
async def profil(ctx ,*, message : str):
    """ [JOUEURS] Affiche le profil SpaceOrigin des JOUEURS, séparer par ' ' """

    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # génération d'un log sur bot-logs
        await log(ctx)
        
        # texte du message d'attente
        tmp_embed = discord.Embed(title="`Veuillez patienter...`", colour=BLUE, url="", description="")
        tmp_embed.set_author(name="SO-INFO", url="", icon_url=URL_ANIM)
        tmp_embed.set_image(url=URLS_WAIT[randint(0,1)])

        # envoie la réponse et le message d'attente sur le même channel
        my_message = await bot.send_message(ctx.message.channel,embed = tmp_embed)
        
        liste_emb = profil_emb(message)
        for e in liste_emb :
            await bot.say(embed=e)
            
        await bot.delete_message(my_message)


@bot.command(pass_context = True)
async def pub(ctx, *args):
    """ [] Fait apparaitre les liens utiles de SpaceOrigin. """
    
    # si on est sur le channel bot ou du staff
    if ctx.message.channel.id == secrets.ID_CHAN_BOT or check_staff(ctx.message):
    
        # génération d'un log sur bot-logs
        await log(ctx)
        
        # envoie le message sur le même channel
        await bot.say(embed = pub_emb())


"""
#########################################################################################
#                            Fonctions d'affichage                                   
#########################################################################################
"""


def rand_emb(liste_nb,mini,maxi,nb_essais):

    # initialisation
    unique = {}
    compteur = 0
    liste_unique = []
    texte = ""
    if nb_essais > 1 :
        tirage_str = " tirages entre "
    else :
        tirage_str = " tirage entre "        
    texte2 = str(nb_essais) + tirage_str + str(mini) + " et " + str(maxi) + " ."
    embed = discord.Embed(title="", colour=YELLOW, url="", description="")
    
    for nb in range(0,len(liste_nb)):
        if liste_nb[nb] in unique.keys():
            unique[liste_nb[nb]] += 1
        else :
            unique[liste_nb[nb]] = 1
        
    # on prépare la string du résultat
    for c in unique.keys():
        liste_unique.append(int(c))
            
    liste_unique.sort()
        
    for cle in liste_unique:
        if unique[cle] == 1 :
            texte += "[" + str(cle) + "]"
        else :
            texte += "[" + str(cle) + "] * " + str(unique[cle])
                
        if compteur < len(liste_unique) - 1 :
            texte += " , "
        else :
            texte += " . "
        compteur += 1
            
    # mise en forme 
    embed.set_author(name="SO-PLAY", url="", icon_url=URL_ANIM)
    embed.set_thumbnail(url=URL_RAND)
    embed.add_field(name="Informations : ", value=texte2,inline=False)
    embed.add_field(name="Résultat : ", value=texte,inline=False)
    
    # renvoie l'embed correspondant    
    return embed
            

def roles_emb(ctx,membre,planete,statut):
    """ renvoie le embed de !roles """
    
    # initialisation
    embed = discord.Embed(title="Mise à jour des rôles", colour=GREEN, url="", description="")
    if membre.avatar : 
        avatar = "https://cdn.discordapp.com/avatars/" + membre.id + "/" + membre.avatar +".png"
    else :
        avatar = "https://cdn.discordapp.com/embed/avatars/" + str(int(membre.discriminator) % 5) + ".png"
    name = membre.name + "#" + membre.discriminator
    
    # mise en forme 
    embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="Joueur : ", value=name,inline=False)
    embed.add_field(name="Planète : ", value=planete,inline=True)
    embed.add_field(name="Statut : ", value=statut,inline=True)
    
    # renvoie l'embed correspondant
    return embed
              
            
def demute_emb(ctx):
    """ renvoie le embed de !demute """
    
    # initialisation
    cible_val = ""
    embed = discord.Embed(title="`Un MUTE se termine !`", colour=RED, url="", description="")
    
    # on récupère le membre et son nom
    m = ctx.message.mentions[0]
    cible_val = m.name + "#" + m.discriminator 
    if m.avatar : 
        avatar = "https://cdn.discordapp.com/avatars/" + m.id + "/" + m.avatar +".png"
    else :
        avatar = "https://cdn.discordapp.com/embed/avatars/" + str(int(m.discriminator) % 5) + ".png"

    # mise ne forme de l'embed
    embed.set_author(name="SO-Tribunal", url="", icon_url=URL_ADMIN)
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text="Il sera sage ;-)", icon_url="")
    embed.set_image(url=URL_DEMUTE)
    embed.add_field(name="Cible : ", value=cible_val,inline=True)

    # renvoie l'embed correspondant
    return embed

def mute_emb(ctx):
    """ renvoie le embed de !mute """
    
    # initialisation
    cible_val = ""
    embed = discord.Embed(title="`Un MUTE est tombé !`", colour=RED, url="", description="")
    
    # on récupère le membre et son nom
    m = ctx.message.mentions[0]  
    cible_val = m.name + "#" + m.discriminator 
    if m.avatar : 
        avatar = "https://cdn.discordapp.com/avatars/" + m.id + "/" + m.avatar +".png"
    else :
        avatar = "https://cdn.discordapp.com/embed/avatars/" + str(int(m.discriminator) % 5) + ".png"

    # mise ne forme de l'embed
    embed.set_author(name="SO-Tribunal", url="", icon_url=URL_ADMIN)
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text="A la prochaine ;-)", icon_url="")
    embed.set_image(url=URL_MUTE)
    embed.add_field(name="Cible : ", value=cible_val,inline=True)

    # renvoie l'embed correspondant
    return embed


def welcome_emb():
    """ renvoie l'embed du message d'accueil """
    
    # initialisation
    embed = discord.Embed(title="`BIENVENUE SUR SO OFFICIEL`", colour=GREEN, url="", description="")
    aFaire = "Passez sur le salon demandes d\'accès pour obtenir vos rôles et ainsi pouvoir parler."
    aFaire += "\nRegardez le message épinglé de ce salon tout est expliqué."
    
    # mise en forme 
    embed.set_author(name="SO-BOT", url="", icon_url=URL_ANIM)
    embed.set_thumbnail(url=URL_ANIM)
    embed.add_field(name="Que faire en arrivant ?", value=aFaire,inline=False)
    embed.set_footer(text="Heureux de vous compter parmis nous ;-)", icon_url="")
    
    # renvoie l'embed correspondant
    return embed
    
    
def me_emb(ctx):
    """ renvoie l'embed correspondant à la commande !me """
  
    # initialisation
    message = ctx.message
    membre = message.author
    roles = []
    t = str(membre.joined_at.strftime("%d/%m/%y  %H:%M"))
    embed = discord.Embed(title="`Votre profil discord`", colour=BLUE, url="", description="")
    if membre.avatar : 
        avatar = "https://cdn.discordapp.com/avatars/" + membre.id + "/" + membre.avatar +".png"
    else :
        avatar = "https://cdn.discordapp.com/embed/avatars/" + str(int(membre.discriminator) % 5)  + ".png"
    
    # on transforme chacun des rôles en str
    roles = get_roles(message,membre)
    roles_str = ""
    nb_roles = len(roles)
    compteur = 0
    for r in roles :
        compteur += 1  
        if compteur != nb_roles :
            roles_str += r + " , "
        else :
            roles_str += r + " ."        
                
    # mise en forme du embed a afficher
    embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text="Heureux de vous avoir aidé ;-)", icon_url="")
    embed.add_field(name="Pseudo : ", value=membre.display_name,inline=True)
    embed.add_field(name="Date d'arrivée : ", value=str(t),inline=True)
    embed.add_field(name="Rôles : ", value=roles_str,inline=False)
    
    # renvoie l'embed 
    return embed


def pub_emb():
    """ renvoie l'embed correspondant à la commande !pub """

    # initialisations
    embed = discord.Embed(title="`Liens et infos utiles`", colour=YELLOW, url="", description="")
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
    embed.set_author(name="SO-PUB", url="", icon_url=URL_ANIM)
    embed.set_thumbnail(url=URL_ANIM)
    embed.add_field(name="Jeu : ", value=URL_JEU,inline=False)
    embed.add_field(name="Support : ", value=URL_SUPPORT,inline=False)
    embed.add_field(name="Shop : ", value=URL_BOUTIQUE,inline=False)
    embed.add_field(name="Tchat : ", value=URL_TCHAT,inline=False)
    embed.add_field(name="Forum : ", value=URL_FORUM,inline=False)
    embed.add_field(name="Discord : ", value=URL_DISCORD,inline=False)
    embed.add_field(name="Facebook : ", value=URL_FACEBOOK,inline=False)

    # s'il y a un event
    if EVENT != "" :
        embed.add_field(name="Event : ", value=EVENT,inline=False)
        
    # gère l'affichage des sites de votes
    texte = ""
    for url in URL_VOTE :
        texte += url + "\n"
    embed.add_field(name="Votez pour Spaceorigin sur : ", value=texte,inline=False)

    # renvoie l'embed
    return embed
    

def profil_emb(message):
    """ renvoie l'embed correspondant à la commande !profil """

    # initialisation
    args = message.split(" ")
    liste_emb = []

    # pour chaque pseudo passé en paramètre
    for j in args :
        courant = Joueur(j)
        
        # si on a un joueur de ce nom
        if courant.pseudo != "" : 
        
            # si la fiche est complète
            if courant.complete :
                embed = discord.Embed(title="", colour=BLUE, url="", description="")
                embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
                embed.set_thumbnail(url=courant.avatar)
                embed.add_field(name="Pseudo : ", value=courant.pseudo,inline=True)
                embed.add_field(name="Race : ", value=courant.race,inline=True)
                embed.add_field(name="Level : ", value=courant.level,inline=True)
                embed.add_field(name="Xp : ", value=courant.xp,inline=True)
                role_pla = courant.planete + " (" +  courant.role_planete + ")"
                embed.add_field(name="Planète : ", value=role_pla,inline=False)
                role_all = courant.alliance + " (" +  courant.role_alliance + ")"             
                embed.add_field(name="Alliance : ", value=role_all,inline=False)
                embed.add_field(name="Rang général : ", value=courant.rang,inline=True)        
                embed.add_field(name="Rang planètaire : ", value=courant.rang_planete,inline=True) 
                embed.add_field(name="Points : ", value=courant.points,inline=False)
                embed.add_field(name="Url : ", value=courant.url, inline = False)
            
            # si fiche incomplète
            else :
                embed = discord.Embed(title="", colour=BLUE, url="", description="")
                embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
                embed.set_thumbnail(url=courant.avatar)
                embed.add_field(name="Pseudo : ", value=courant.pseudo,inline=True)
                embed.add_field(name="Race : ", value=courant.race,inline=True)
                embed.add_field(name="Level : ", value=courant.level,inline=True)
                embed.add_field(name="Xp : ", value=courant.xp,inline=True)
                embed.add_field(name="Planète : ", value=courant.planete,inline=False)
                embed.add_field(name="Rang général : ", value=courant.rang,inline=True)        
                embed.add_field(name="Rang planètaire : ", value=courant.rang_planete,inline=True) 
                embed.add_field(name="Url : ", value=courant.url, inline = False)
        
        # le pseudo n'appartient a aucun joueur
        else :
            embed = discord.Embed(title="", colour=RED, url="", description="")
            embed.set_author(name="SO-INFO", url="", icon_url=URL_MOD_FORUM)
            error = "Le joueur " + j + " n'éxiste pas..."
            embed.add_field(name="Error : ", value=error,inline=False)
        
        liste_emb.append(embed)
        
    # renvoie les embeds
    return liste_emb


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


