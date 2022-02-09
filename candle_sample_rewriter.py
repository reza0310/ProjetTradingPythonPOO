import finnhub
import datetime
import os

with open("clef.txt", "r") as f:
    clef = f.readline()

finnhub_client = finnhub.Client(api_key=clef)

debut = 1600000000
fin = 1640000000

date_debut, heure_debut = str(datetime.datetime.fromtimestamp(debut)).split(" ")
date_debut = date_debut.split("-")
date_fin, heure_fin = str(datetime.datetime.fromtimestamp(fin)).split(" ")
date_fin = date_fin.split("-")

print("Récupération et insertion des données allant du", date_debut[2]+"/"+date_debut[1]+"/"+date_debut[0], "à", heure_debut, "au", date_fin[2]+"/"+date_fin[1]+"/"+date_fin[0], "à", heure_fin)

path = os.path.dirname(__file__)
print("PATH:", path[:path.rfind("/")]+"/candle_sample.txt")
with open(path[:path.rfind("/")]+"/candle_sample.txt", "w+") as f:
    f.truncate(0)
    f.write(str(finnhub_client.stock_candles('AAPL', 1, debut, fin)))