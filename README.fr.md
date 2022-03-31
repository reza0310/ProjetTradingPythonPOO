# Python Trading Bot Project

## Index
- [Pourquoi?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#pourquoi)
- [Versions](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#versions)
- [Comment l'installer et l'utiliser?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#comment-linstaller-et-lutiliser)
- [Description fichier par fichier](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#description-fichier-par-fichier)
- [Comment contribuer?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#comment-contribuer)
- [FAQ](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#faq)
- [Nous contacter](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#nous-contacter)
- [License](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#license)
- [Dernière mise à jour de la documentation](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#dernière-mise-à-jour-de-la-documentation)

## Pourquoi?
Ce projet est un projet scolaire. La consigne était de faire un bot de trading capable d'amasser un max de thunes à partir de données quelconques. Les données proviennent de "https://finnhub.io/docs/api/stock-candles". Ce bot n'as pas été conçu pour être utilisé sur de vrais marchés ou quoi que ce soit du genre. Il n'est en rien garanti et conçu dans un objectif de travail informatique par des personnes peu voire pas qualifiées en trading. N'essayez pas d'en tirer de l'argent vous riqueriez de tout perdre.

## Versions
0.0: En développement (ne fonctionne pas).<br>
1.1: Première version viable avec deux stratégies.<br>
1.2: Ajout de plus de stratégies et tests sur divers jeux de données pour voir l'adaptabilité de chacune de nos stratégies à la variation des données sachant que le jeu de données de l'éval ne sera pas celui qu'on nous a donné (testé sur littéralement toutes les données disponibles).<br>
1.3: Ajout d'une représentation visuelle des différentes actions et de l'argent de notre bot par dessus et décision d'utiliser la stratégie 1 suite aux tests précédents (version actuelle et finale).<br>

## Comment l'installer et l'utiliser?
Pour cette section, nous allons assumer que vous savez utiliser un ordinateur mais ne savez rien de la programmation. Si c'est le cas et que vous vous retrouvez bloqués, [contactez-nous](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#nous-contacter).

Premièrement, vous aurez besoin de Python. Pour ce faire, regardez [mon tutoriel sur comment faire](https://github.com/reza0310/Tutorials/blob/python/README.en.md).<br>
Bravo! Vous avez désormais Python!

La prochaine étape est d'installer le projet parent. Téléchargez-le depuis [le dépôt de notre professeur](https://github.com/benjaminforest/beagleboys) et dézippez-le n'importe où. Pour les plus qualifiés d'entre vous qui trouvent que c'est beaucoup trop juste pour lancer un objet gardez bien en tête que ça a été prévu pour mettre plein de bots comme le notre en compétition.<br>
Bravo! Vous avez désormais le projet parent!

La dernière étape est d'installer le projet enfant c'est à dire le notre. Téléchargez-le en tant que ZIP comme vous l'avez fait pour le projet parent depuis [ce lien](https://github.com/reza0310/ProjetTradingPythonPOO) (qui est probablement le lien duquel vous venez...). Ensuite, extrayez-le dans le dossier du projet parent. Si ça vous demande si vous voulez remplacer des fichiers dites oui.<br>
Bravo! Vous avez désormais terminé l'installation!

Maintenant, pour le lancer, regardez la [description fichier par fichier](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#description-fichier-par-fichier) quel script executer en fonction de ce que vous voulez faire.

## Description fichier par fichier
- [.gitignore](https://github.com/benjaminforest/beagleboys/blob/main/.gitignore): Fichier listant les différents fichiers et dossiers que vous ne voulez pas mettre sur git / github (caches, fichiers secret, ...) (Principalement utile quand l'upload est automatisé avec des logiciels comme Github Desktop pour pas qu'ils incluent ces fichiers dans vos commits).
- [.gitmodules](https://github.com/benjaminforest/beagleboys/blob/main/.gitmodules): Liens vers les projets des autres étudiants pour les faire apparaître sur le dépôt du prof.
- [README.md](https://github.com/benjaminforest/beagleboys/blob/main/README.md): Informations a destination des étudiants.
- [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py): Un exemple simple de bots conçu par notre prof à titre de démonstration (dont notre bot hérite juste pour la ligne 9 et le défi XD)
- [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py): Client utilisé par les bots participants pour acheter et vendre des actions. Ca permet au prof de vérifier que nous ne trichions pas en faisant une interface immuable entre notre bot et ses actions restreignant au passage certaines choses comme le faites que nous ne puissions pas acheter des actions que nous n'avons pas les moyens d'acheter. Nous donne aussi accès à des informations sur l'argent et les actions en notre possession.
- [candle_sample.txt](https://github.com/benjaminforest/beagleboys/blob/main/candle_sample.txt): Quelques exemples de données pour tester nos bots.
- [collect_candles.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles.py): Exécutable mais lent et pas vraiment très à jour... Un vieux script pour récupérer des données.
- [collect_candles2.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles2.py): Exécutable. Le véritable script permettant de collecter des données. Les lignes 10 et 13 indiquent les horodates de début et de fin entre lesquelles collecter des données. La version gratuite de l'API ne nous permet que de collecter les données qu'un mois à la fois, d'aujourd'hui à il y a un an.
- [collect_data.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_data.py): Exécutable mais inutile. Un autre document de collecte de données. Si vous rencontrez des erreurs, vérifiez que vous avez [le bon module](https://stackoverflow.com/questions/42905748/i-am-getting-attribute-error-module-object-has-no-attribute-enabletrace-whi). Ce script ne sauvegarde les données que 100 par 100 et ne récupère pas les prix de fermeture qui sont les plus utilisés.
- [gui.py](https://github.com/benjaminforest/beagleboys/blob/main/gui.py): Exécutable mais inutile. Un exemple d'interface graphique pour aider les étudiants qui en ont besoin a faire le leur.
- [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py): EXÉCUTABLE. Le coeur du programme. Lie chacun de nos bots à une instance du [client / coursier](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py) et utilisant [le script shared.py du dossier "shared"](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py) pour tout en fait le fichier en lui-même est quasiment vide en soit... Je ne pense pas que l'objectif à la base était juste de casser le fichier surtout sachant le script vide dans le dossier shared.py m'enfin le projet est presque terminé pour notre groupe-classe donc bon...
- [main_simple.py](https://github.com/benjaminforest/beagleboys/blob/main/main_simple.py): Une version qui se veut plus simple du fichier [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py). Pourrais être exécutable si [notre prof](https://github.com/benjaminforest) acceptais [la demande de modification #4](https://github.com/benjaminforest/beagleboys/pull/4).
- DOSSIER: [shared](https://github.com/benjaminforest/beagleboys/tree/main/shared) (Un dossier contenant le gros du code du fichier main.py)
    - [\_\_init__.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/__init__.py): Fichier vide. (N'existe peut-être plus si [notre prof](https://github.com/benjaminforest) a accepté [la demande de modification #3](https://github.com/benjaminforest/beagleboys/pull/3)).
    - [shared.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py): Fonctions qui sont basiquement l'entièreté du code du fichier [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py).
- FOLDER: [ProjetTradingPythonPOO](https://github.com/reza0310/ProjetTradingPythonPOO) (Le projet de mon équipe)
    - [.gitignore](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/.gitignore): Fichier listant les différents fichiers et dossiers que vous ne voulez pas mettre sur git / github (caches, fichiers secret, ...) (Principalement utile quand l'upload est automatisé avec des logiciels comme Github Desktop pour pas qu'ils incluent ces fichiers dans vos commits).
    - [LICENSE](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE): Fichier administratif listant vos droits et devoirs vis-à-vis de notre travail.
    - [README.en.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md): Fichier expliquant le projet en anglais.
    - [README.fr.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md): Fichier expliquant le projet en français. C'est le fichier que vous êtes actuellement en train de lire.
    - [README.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.md): Fichier reliant les README de toutes les langues.
    - [bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py): Le bot de mon équipe. Ne peut être exécuté directement. hérite de [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py) pour l'attribut self.client qui est une instance du [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py). Utilise [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) pour communiquer avec [ProjetTradingPythonPOO/graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py).
    - [collect_candles.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/collect_candles.py): Ma propre version du fichier [collect_candle.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles.py) basé que l'expression de la volonté / de l'objectif de notre prof pendant qu'il faisait collect_candles2 parce qu'il voulait changer la structure des fichiers et que notre bot utilisait déjà la structure de fichiers précédente et que je voulais l'adapter au plus vite.
    - [globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py): Un petit fichier définissant quelque variables ultra-globales pour faire communiquer [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) et [ProjetTradingPythonPOO/graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py).
    - [graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py): EXÉCUTABLE. Utilise [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) pour informer [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) (qui hérite de [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py)) de collecter, pendant son exécution, les données nécessaires à faire les affichages (en utilisant la booléenne "affichage"). Ensuite, fait une copie de [candle_sample.txt](https://github.com/benjaminforest/beagleboys/blob/main/candle_sample.txt) à l'emplacement [ProjetTradingPythonPOO/candle_sample.txt](https://github.com/benjaminforest/beagleboys/blob/main/candle_sample.txt) avant d'exécuter [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py) (qui utilises [shared/shared.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py) et connecte les bots au [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py)) pour permettre au [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) de collecter les données concernant les chandelles et, surtout, lui-même. Après cette exécution cruciale, le script demande à [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) les données et les arrangent en des affichages cools pour chaque symbole montrant la variation du cours de ce symbole et l'argent (en monnaie et en actions combinées) au cours du temps. Je sais qu'il y a beaucoup de fichiers en jeu mais basiquement c'est le fichier que vous cherchez si vous voulez juste voir des résultats stylé XD. Agit littéralement en sur-couche du fichier [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py).
    - [A_year_worth_of_data.zip](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/A_year_worth_of_data.zip): Fichier réalisé avec douze utilisations du fichier [collect_candles2.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles2.py) le 14/02/2022 A des fins d'archivage et dépassement des capacités de l'API. Contient probablement toutes les données de 14/02/2021 à 14/02/2022.
- Tout les autres dossiers sont les projets d'autres étudiants que je n'ai pas étudié et que je peux (ni ne veux en vrai j'ai autre chose à faire et c'est pas mon rôle) documenter.

## Comment contribuer?
Sachant qu'il s'agit d'un projet scolaire, seuls les camarades de mon groupe de travail son autorisés à participer. Si vous avez vraiment très envie de modifier des choses je ne peux que vous conseiller de faire une fork et si vous voulez que je publie vos modifications pour une raison ou pour une autre [venez en discuter avec moi](https://github.com/reza0310/ProjetTradingPythonPOO#contact-us).<br>
Malgré cela, vous pouvez quand même nous aider en ouvrant des rapports de problèmes (bugs, demandes, ...) sur la [page dédiée](https://github.com/reza0310/ProjetTradingPythonPOO/issues)! Si vous le faites, merci beaucoup!

## FAQ
Aucune question ne nous a encore été posée.

## Nous contacter
reza0310: [page de contact](https://github.com/reza0310#a-propos-de-mon-profil).

## License
Lisez le [fichier "LICENSE"](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE) (en anglais).

### Dernière mise à jour de la documentation 
Mardi 1 mars 2022
