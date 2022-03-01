# Importation de quelques modules nécessaires pour ajouter le dossier parent au chemin de recherche de l'import pour importer l'objet du prof à hériter
import os
import sys
import json
import globals
import datetime
# Récupération du path (Chemin de fichier) du script actuel (bot.py):
# -La variable __file__ est un objet désignant le fichier actuel
# -os.path.dirname() permet d'en extraire le path

# Exemple de path: D:/GitHub/beagleboys/main.py
path = os.path.dirname(__file__)
# Ajout du path du dossier parent à la liste de recher d'importe:
# -os.sep est une variable contenant le séparateur de path de notre système d'exploitation (/ pour Linux, \ pour windows, ...)
# -path[:path.rfind(os.sep)] permet d'extraire une sous-chaîne en l'occurence la partie de path allant jusqu'à son dernier os.sep
# -sys.path.append() permet d'ajouter le path nouvellement créé aux chemins de recherche de l'import
sys.path.append(path[:path.rfind(os.sep)])
# On importe beaglebot
import beaglebot

# On en hérite
class Bot(beaglebot.BeagleBot):

    # On défini les attributs utiles
    def __init__(self, *args):
        super(Bot, self).__init__(*args)
        self.listes_variations = []
        for i in range(len(globals.symboles)):
            self.listes_variations.append([0, 0])
        self.listes_valeurs = []
        for i in range(len(globals.symboles)):
            self.listes_valeurs.append([0])
        self.actions = []
        for i in range(len(globals.symboles)):
            self.actions.append(0)
        self.achetes = []

    # Fonction qui gère les chandelles de données
    def process_candle(self, candle_msg):
        # On convertit la candle récupérée sous forme textuelle en dictionnaire
        candle_data = json.loads(candle_msg)
        symbole = [x for x in candle_data.keys()][0]
        # On en vérifie la validité (Présence de donnée et apparatenance au repère AAPL
        if candle_data[symbole]['s'] == "ok":
            # On se simplifie la tâche en préselectionnant le repère
            candle_data = candle_data[symbole]
            # On récupère certaines données utiles
            variation = round(candle_data['c']-candle_data['o'], 2)
            indice = globals.symboles.index(symbole)
            # Si graph.py nous le demande, on collecte des données d'affichage
            if globals.affichage:
                globals.data[indice][0].append(candle_data['o'])
                globals.data[indice][1].append(candle_data['c'])
                globals.data[indice][2].append(candle_data['h'])
                globals.data[indice][3].append(candle_data['l'])
                globals.data[indice][4].append(datetime.datetime.fromtimestamp(candle_data['t']).strftime("%d/%m/%y %HH%M"))
                globals.argent.append(100000+self.client.gains())
            # On applique notre stratégie (la n°1)
            self.strategie1(candle_data, variation, indice, symbole)
            #self.strategie2(candle_data, indice, symbole)
            #self.strategie3(candle_data, indice, symbole)
            #self.strategie4(candle_data, variation, indice, symbole)
            
            # On enregistre
            self.listes_variations[indice].append(variation)
            self.listes_valeurs[indice].append(candle_data['c'])

    # Fonction utilisée par la stratégie 2 pour récupérer les prix moyens sur une période donnée mais la période dépend beaucoup trop du jeu de données
    def moyenne(self, periode, indice):
        if periode == "court":
            sub = self.listes_valeurs[indice][-(len(self.listes_valeurs[indice])//20):]
        elif periode == "moyen":
            sub = self.listes_valeurs[indice][-(len(self.listes_valeurs[indice])//10):]
        elif periode == "long":
            sub = self.listes_valeurs[indice][-(len(self.listes_valeurs[indice])//5):]
        return sum(sub)/len(sub)

    # Les 4 fonctions suivantes sont nos stratégies. Plutôt explicite n'est-ce pas?
    def strategie1(self, candle_data, variation, indice, symbole):
        if self.client.money > candle_data['c'] and variation < self.listes_variations[indice][-1] < 0:
            somme = (self.client.money * 0.5) // candle_data['c']
            self.client.buy(symbole, somme)
            self.actions[indice] += somme
        elif variation > self.listes_variations[indice][-1] > 0:
            self.client.sell(symbole, self.actions[indice])
            self.actions[indice] = 0

    def strategie2(self, candle_data, indice, symbole):
        if self.client.money > candle_data['c'] and self.moyenne('court', indice) < self.moyenne('long', indice):
            somme = self.client.money // candle_data['c']
            self.client.buy(symbole, somme)
            self.actions[indice] += somme
        elif self.moyenne('court', indice) > self.moyenne('long', indice):
            self.client.sell(symbole, self.actions[indice])
            self.actions[indice] = 0

    def strategie3(self, candle_data, indice, symbole):
        if symbole not in self.achetes:
            somme = (self.client.money * 0.16) // candle_data['c']
            self.client.buy(symbole, somme)
            self.actions[indice] += somme
            self.achetes.append(symbole)

    def strategie4(self, candle_data, variation, indice, symbole):
        if self.client.money > candle_data['c'] and variation < self.listes_variations[indice][-1] < self.listes_variations[indice][-2] < 0:
            somme = (self.client.money * 0.3) // candle_data['c']
            self.client.buy(symbole, somme)
            self.actions[indice] += somme
        elif variation > self.listes_variations[indice][-1] > self.listes_variations[indice][-2] > 0:
            self.client.sell(symbole, self.actions[indice])
            self.actions[indice] = 0
