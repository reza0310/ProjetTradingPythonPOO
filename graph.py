import os
import sys
import shutil
import globals
import pandas


if __name__ == "__main__":
    globals.affichage = True

    # On récupère le path du dossier parent dans lequel résident les fichiers de lancement
    path = os.path.dirname(__file__)
    path = path[:path.rfind('/')]

    # On récupère le fichier de données nécessaire
    shutil.copy(path+"/candle_sample.txt", "candle_sample.txt")

    # On lance le bot normalement avec juste une variable différente
    sys.path.append(path)
    import main
    dataframes = []
    for i in range(len(globals.symboles)):
        dataframes.append([])
        dataframes[i] = pandas.DataFrame({'open': globals.data[i][0],
                       'close': globals.data[i][1],
                       'high': globals.data[i][2],
                       'low': globals.data[i][3]},
                       index=globals.data[i][4])
    print(dataframes[0])