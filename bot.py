# Importation de quelques modules nécessaires pour ajouter le dossier parent au chemin de recherche de l'import pour importer l'objet du prof à hériter
import os
import sys
import json
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

    def __init__(self, *args):
        super(Bot, self).__init__(*args)
        self.symboles = ["AAPL", "TSLA", "ATVI", "DIS", "AMZN", "BINANCE:BTCUSDT"]
        self.listes = []
        for i in range(len(self.symboles)):
            self.listes.append([0])
        self.actions = []
        for i in range(len(self.symboles)):
            self.actions.append(0)

    def process_candle(self, candle_msg):
        # On convertit la candle récupérée sous forme textuelle en dictionnaire
        candle_data = json.loads(candle_msg)
        symbole = [x for x in candle_data.keys()][0]
        # On en vérifie la validité (Présence de donnée et apparatenance au repère AAPL
        if candle_data[symbole]['s'] == "ok":
            # On se simplifie la tâche en préselectionnant le repère
            candle_data = candle_data[symbole]
            v = round(candle_data['c']-candle_data['o'], 2)
            indice = self.symboles.index(symbole)
            if v < 0 and v < self.listes[indice][-1] and self.listes[indice][-1] < 0:
                somme = (self.client.money*0.5)//candle_data['c']
                self.client.buy(symbole, somme)
                self.actions[indice] += somme
            elif self.client.money > candle_data['c'] and v > 0 and v > self.listes[indice][-1] and self.listes[indice][-1] > 0:
                self.client.sell(symbole, self.actions[indice])
                self.actions[indice] = 0
            self.listes[indice].append(v)