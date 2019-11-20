"""

    Auteur: xR3m1x
    Date : 17 Novembre 2019
    Version du programme : 1.0
        Entrainement d'unités pour attaquer basiquement la reine.

    But du programme :
        Construire des bâtiments et créer des armées pour détruire la Reine de votre adversaire.

"""
import sys
import math


#--------------------------------------------------
###### CLASSES ######
## Classe représentant les entités de manières générales (sites et unités)
class Entite :
    # Fonction d'initialisation de la classe 'Entite'
    def __init__(self, x, y, owner) :
        self.x = x                      # Coordonnée 'x' de l'entite
        self.y = y                      # Coordonnée 'y' de l'entite
        self.owner = owner              # Proprietaire de l'entite

## Classe représentant les unités (reines, chevalier, archer)
class Unite(Entite):
    # Fonction d'initialisation de la classe 'Unite'
    def __init__(self, x, y, owner, pv, typeUnit) :
        super().__init__(x,y,owner)
        self.pv = pv                    # Point de vie de l'unite
        self.typeUnit = typeUnit        # Type de l'unite (-1: Reine, 0: Chevalier, 1: Archer)

## Classe représentant les sites (site vierge ou batiment)
class Site(Entite):
    # Fonction d'initialisation de la classe 'Site'
    def __init__(self, id, x, y, radius, typeSite, cycleTrain, ignore1, ignore2) :
        self.id = id                    # Identifiant du site
        super().__init__(x, y, -1)
        self.typeSite = typeSite        # Type du site (-1: vide, 0: Chevalier, 1: Archer)
        self.radius = radius            # Rayon du site
        self.cycleTrain = cycleTrain    # Tour restant avant fin entrainement en cours
        self.ignore1 = ignore1          # Ignore pour le moment
        self.ignore2 = ignore2          # Ignore pour le moment

## Classe représentant les elements globaux du jeu
class Challenge :
    # Fonction d'initialisation de la classe 'Challenge'
    def __init__(self, nbSites) :
        self.po = 100                   # Pieces d'or du joueur
        self.nbSites = nbSites          # Nombre de sites present sur la carte
        self.nbEntite = 0               # Nombre d'unites actives
        self.units = []                 # Liste des unites
        self.site = []                  # Liste des sites
        self.siteInfo = []              # informations de chaque site
    # Fonction remettant a zero la liste des unites
    def raz_unit(self) :
        self.units = []
    # Fonction mettant à jour l'argent disponible
    def set_po(self, po) :
        self.po = po
    # Fonction retournant l'argent disponible
    def get_po(self) :
        return self.po
#--------------------------------------------------
#--------------------------------------------------
###### CONSTANTES ######
VIDE = -1
CASERNE = 2

ALLIE = 0
ENNEMI = 1

REINE = -1
CHEVALIER = 0
ARCHER = 1
#--------------------------------------------------
#--------------------------------------------------
###### Initialisation ######
challenge=Challenge(int(input()))
#--------------------------------------------------

for i in range(challenge.nbSites):
    site_id, x, y, radius = [int(j) for j in input().split()]

#--------------------------------------------------
    challenge.site.append(Site(site_id, x, y, radius,-1,-1,1,1))
#--------------------------------------------------

# Tour de jeu
while True:
    gold, touched_site = [int(i) for i in input().split()]

#--------------------------------------------------
    challenge.set_po(gold)
#--------------------------------------------------

    for i in range(challenge.nbSites):
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]

#--------------------------------------------------
        
#--------------------------------------------------

    num_units = int(input())

#--------------------------------------------------
    # RaZ de la liste des unites
    challenge.raz_unit()
#--------------------------------------------------

    for i in range(num_units):
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        
#--------------------------------------------------
        challenge.units.append(Unite(x, y, owner, health, unit_type))
#--------------------------------------------------
    # Première ligne : Action de la reine
    # Seconde ligne : Instructions d'entrainement
    print("WAIT")
    print("TRAIN")