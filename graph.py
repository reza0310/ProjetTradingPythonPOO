import os
import sys
import shutil
import globals
import pandas
sys.path.append("C:\\users\\dupre\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

    for i in range(len(globals.symboles)):
        print("Traitement du symbole", globals.symboles[i])

        print("Initialisation de la figure (code pris ici: https://towardsdatascience.com/the-simplest-way-to-create-an-interactive-candlestick-chart-in-python-ee9c1cde50d8)...")
        plot1 = go.Candlestick(x=globals.data[i][4],
                               name="Chandelles",
                               open=globals.data[i][0],
                               high=globals.data[i][2],
                               low=globals.data[i][3],
                               close=globals.data[i][1])

        plot2 = go.Scatter(
            x=globals.data[i][4],
            y=globals.argent,
            name='Notre argent',
            marker=dict(
                color='rgb(34,163,192)'
            )
        )

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(plot1)
        fig.add_trace(plot2, secondary_y=True)

        fig.update_layout(
            title=f"{globals.symboles[i]}'s adjusted stock price",
            yaxis_title="Prix ($)",
            xaxis_title="Temps"
        )

        print("Affichage...")
        fig.show()