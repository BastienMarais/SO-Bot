#coding: utf-8
#########################################################################################
#   Description :   Ce programme permet de récupérer le profil des joueurs de SO
#   File :          player.py
#   Usage :         python3 player.py
#   Requirements :  pip install bs4 requests
#   User.name :     Bastien Marais
#   User.email :    marais.bas@gmail.com                        
#   Ressources :    https://zestedesavoir.com/billets/2057/scraper-des-donnees-sur-une-page-web-en-python-avec-beautifulsoup-1/
#                   http://apprendre-python.com/page-beautifulsoup-html-parser-python-library-xml
#########################################################################################


"""
#########################################################################################
#                            Différents imports                                      
#########################################################################################
"""


import requests
from bs4 import BeautifulSoup


"""
#########################################################################################
#                            Class Joueur                                      
#########################################################################################
"""
    

class Joueur :
    """ Un joueur est caractérisé par :
        self.pseudo
        self.race
        self.planete
        self.level
        self.xp
        self.points
        self.rang
        self.rang_planete
        self.alliance
        self.role_alliance
        self.role_planete
        self.url
    """
    
    def __init__(self,pseudo):
        """ constructeur """
        
        # initialisation
        pseudo = pseudo.lower()
        self.pseudo = ""
        self.race = ""
        self.planete = ""
        self.level = ""
        self.xp = ""
        self.points = ""
        self.rang = ""
        self.rang_planete = ""
        self.alliance = ""
        self.role_planete = ""
        self.role_alliance = ""
        self.url = ""
        
        
         # il on récupère les infos de base
        self.url = "http://bigbang.spaceorigin.fr/profile/" + pseudo
        requete = requests.get(self.url)
        page = requete.content
        soup = BeautifulSoup(page, "lxml")
        
        self.pseudo = soup.find("div", {"id": "username"}).string
        self.race = soup.find("div", {"id": "race", "class" : "value"}).string
        self.planete = soup.find("div", {"id": "planet"}).get("alt")
        self.level = soup.find("div", {"id": "level", "class" : "value"}).string
        self.xp = soup.find("div", {"id": "xp", "class" : "value"}).string
        self.rang = soup.find("div", {"id": "rank", "class" : "value"}).string
        self.rang_planete = soup.find("div", {"id": "planet_rank", "class" : "value"}).string
        
        # on tente de compléter les infos avec le mur des joueurs
        requete = requests.get("http://bigbang.spaceorigin.fr/players")
        page = requete.content
        soup = BeautifulSoup(page, "lxml")
        href = "/profile/" + pseudo
        fiche_perso = soup.find("a", {"href" : href})
           
        # si on a trouvé une fiche
        if fiche_perso :
            # récupération des données
            self.points = fiche_perso.find("div", {"class" : "wall-item-points" }).string
            self.alliance = fiche_perso.find("div", {"class" : "wall-item-alliance-name" }).string
            
            # table d'équivalence des class html avec les rôles
            roles = {}
            roles["finance_minister"] = "Ministre de l'économie"
            roles["foreign_affairs_minister"] = "Ministre de la diplomatie"
            roles["governor"] = "Empereur"
            roles["interior_minister"] = "Ministre de l'intérieur"
            roles["finance_minister_deputy"] = "Ministre de l'économie suppléant"
            roles["foreign_affairs_minister_deputy"] = "Ministre de la diplomatie suppléant"
            roles["governor"] = "Empereur"
            roles["interior_minister_deputy"] = "Ministre de l'intérieur suppléant"
            roles["prime_minister"] = "Premier ministre"
            roles[""] = "Citoyen"
   
            # liste des class html correspondant au rôle dans l'alliance
            r_alli = {}
            r_alli["member"] = "Membre"
            r_alli["manager"] = "Gestionnaire"
            r_alli["leader"] = "Chef"
            r_alli[""] = "Sans alliance"
            
            # on teste toutes les combinaisons 
            for r in roles.keys():
                for a in r_alli.keys() :
                    c = "wall-item-badge " + a + " " + r 
                    test = fiche_perso.find("div", {"class" : c })
                    
                    # si un test est concluant, on lui assigne le role
                    if test :
                        self.role_planete = roles[r]
                        self.role_alliance = r_alli[a]

        # si originel
        if self.race == "Inconnu" :
            self.race = "Originel"
            
            
    def __str__(self):
        """ renvoie la string automatiquement lors des conversions en str """
        
        texte = "```md\n"
        texte += "# Pseudo : " + self.pseudo + "\n"
        texte += "Race : " + self.race + "\n"
        
        # ajout ou non des champs liés a l'alliance
        if self.alliance != "" :
            if self.role_alliance != "" :
                texte += "Alliance : " + self.alliance + " (" + self.role_alliance + ")\n"
            else :
                texte += "Alliance : " + self.alliance + "\n"
            
        # ajout ou non de rôle sur la planète
        if self.role_planete != "" :
            texte += "Planète : " + self.planete + " (" + self.role_planete + ")\n"
        else :
            texte += "Planète : " + self.planete + "\n"
            
        texte += "Rang général : " + self.rang + "\n"
        texte += "Rang planètaire : " + self.rang_planete + "\n"
        texte += "Level : " + self.level + "\n"
        texte += "Xp : " + self.xp + "\n"
        
        # si on a récupéré les infos de la 2ème page
        if self.points != "" :
            texte += "Points : " + self.points + "\n"
            
        texte += "Url : " + self.url + "\n"
        texte += "```"
    
        # renvoie la str correspondant au Joueur
        return texte

