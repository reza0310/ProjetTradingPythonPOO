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

    def process_candle(self, candle_msg):
        # On convertit la candle récupérée sous forme textuelle en dictionnaire
        candle_data = json.loads(candle_msg)
        # On en vérifie la validité (Présence de donnée et apparatenance au repère AAPL
        if "AAPL" in candle_data.keys() and candle_data['AAPL']['s'] == "ok":
            # On se simplifie la tâche en préselectionnant le repère
            candle_data = candle_data['AAPL']
            print('Data:', candle_data)
            # On parcourt toutes les données qui peuvent arriver par plusieurs de notre candle
            for i in range(len(candle_data['t'])):
                print("Variation totale du prix:", round(candle_data['h'][i]-candle_data['l'][i], 2), "€")
                v = round(candle_data['c'][i]-candle_data['o'][i], 2)
                print("Variation au cours de la journée:", "+" if v > 0 else "", str(v), "€")