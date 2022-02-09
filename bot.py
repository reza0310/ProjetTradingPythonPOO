# Importation de quelques modules nécessaires pour ajouter le dossier parent au chemin de recherche de l'import pour importer l'objet du prof à hériter
import os, sys
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
        super().process_candle(candle_msg)