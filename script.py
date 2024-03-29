"""

    Auteur: xR3m1x
    Date : 01 Decembre 2019
    Version du programme : Bronze
        A définir....

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
    def __init__(self, id, x, y, owner, radius, typeSite, cycleTrain, typeArmy, gold, maxMineProd) :
        self.id = id                    # Identifiant du site
        super().__init__(x, y, owner)
        self.typeSite = typeSite        # Type du site (-1: Vide, 0: Mine, 1: Tour, 2: Caserne)
        self.radius = radius            # Rayon du site
        self.cycleTrain = cycleTrain    # Tour restant avant fin entrainement en cours
        self.typeArmy = typeArmy        # Type d'unite produite (-1: Vide, 0: Chevalier, 1: Archer, 2: Geant)
        self.gold = gold                # Quantité d'or restant à produire par une mine (-1 si inconnue)
        self.maxMineProd = maxMineProd  # Taux de production maximum d'une mine (-1 si inconnue)
    # Fonction mettant à jour les informations
    def maj_site(self, typeSite, owner, cycleTrain, typeArmy):
        self.typeSite = typeSite
        self.owner = owner
        self.cycleTrain = cycleTrain
        self.typeArmy = typeArmy

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
MINE = 0
TOUR = 1
CASERNE = 2

ALLIE = 0
ENNEMI = 1

REINE = -1
CHEVALIER = 0
ARCHER = 1
GEANT = 2
#--------------------------------------------------
#--------------------------------------------------
###### Initialisation ######
challenge=Challenge(int(input()))
#--------------------------------------------------

for i in range(challenge.nbSites):
    site_id, x, y, radius = [int(j) for j in input().split()]

#--------------------------------------------------
    challenge.site.append(Site(site_id, x, y, VIDE, radius,VIDE, VIDE, VIDE,VIDE, VIDE))
    # Position initiale de la reine
    startX = startY = -1
#--------------------------------------------------

# Tour de jeu
while True:
    gold, touched_site = [int(i) for i in input().split()]

#--------------------------------------------------
    challenge.set_po(gold)
    nbKnight = 0
    nbArcher = 0
    nbTour = 0
    nbMine = 0
    tower = {'idTower': -1, 'radius': 2000}
#--------------------------------------------------

    for i in range(challenge.nbSites):
        site_id, gold, maxMineProd, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]

#--------------------------------------------------
        challenge.site[site_id].maj_site(structure_type, owner, param_1, param_2)
        if owner == ALLIE :
            if param_2 == CHEVALIER :
                nbKnight += 1
            elif param_2 == ARCHER :
                nbArcher +=1
            if structure_type == TOUR :
                nbTour += 1
                if param_2<tower['radius'] :
                    tower['idTower'] = site_id
                    tower['radius'] = param_2
            elif structure_type == MINE :
                nbMine += 1
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
        if unit_type == REINE and owner == ALLIE:
            if startX == -1 :
                startX = x
                startY = y
            
            queen = {'xQueen': x, 'yQueen': y}
#--------------------------------------------------

#-------------------------------------------------#
#-------------------------------------------------#
#####           CALCUL DES ACTIONS            #####
#-------------------------------------------------#
#-------------------------------------------------#
    # Parmi la liste de site
    closestSite = {'idClosest': -1, 'dist': 10000}
    # RaZ de la liste des sites disponibles pour l'entrainement
    listTrain = []
    for i in challenge.site :
        # Recherche du site vierge le plus près
        if closestSite['dist'] > math.sqrt((i.x-queen['xQueen'])**2+(i.y-queen['yQueen'])**2) and i.typeSite == VIDE:
            closestSite['idClosest'] = i.id
            closestSite['dist'] = math.sqrt((i.x-queen['xQueen'])**2+(i.y-queen['yQueen'])**2)
        # Recupération des sites disponibles à l'entrainement
        if i.cycleTrain==0 and i.owner==0:
            listTrain.append(i.id)

    # Première ligne : Action de la reine
    if nbKnight >= 1 and nbMine >= 3 :
        if nbTour < 3 :
            print("BUILD {} TOWER".format(closestSite['idClosest']))
        else :
            print("BUILD {} TOWER".format(tower['idTower']))
    elif nbMine < 3 :
        print("BUILD {} MINE".format(closestSite['idClosest']))
    elif nbKnight < 1 :
        print("BUILD {} BARRACKS-KNIGHT".format(closestSite['idClosest']))
        
    # Seconde ligne : Instructions d'entrainement
    print("TRAIN",*listTrain[:challenge.po//80],sep=' ')