# Python Trading Bot Project

## Index
- [Pourquoi?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#pourquoi)
- [Versions](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#versions)
- [Comment l'installer et l'utiliser?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#comment-l'installer-et-l'utiliser)
- [Description fichier par fichier](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#description-fichier-par-fichier)
- [Comment contribuer?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#comment-contribuer)
- [FAQ](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#faq)
- [Nous contacter](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#nous-contacter)
- [License](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#license)
- [Dernière mise à jour de la documentation](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#derniere-mise-a-jour-de-la-documentation)

## Pourquoi?
Ce projet est un projet scolaire. La consigne était de faire un bot de trading capable d'amasser un max de thunes à partir de données quelconques. Les données proviennent de "https://finnhub.io/docs/api/stock-candles". Ce bot n'as pas été conçu pour être utilisé sur de vrais marchés ou quoi que ce soit du genre. Il n'est en rien garanti et conçu dans un objectif de travail informatique par des personnes peu voire pas qualifiées en trading. N'essayez pas d'en tirer de l'argent vous riqueriez de tout perdre.

## Versions
0.0: En développement (ne fonctionne pas).<br>
1.1: Première version viable avec deux stratégies.<br>
1.2: Ajout de plus de stratégies et tests sur divers jeux de données pour voir l'adaptabilité de chacune de nos stratégies à la variation des données sachant que le jeu de données de l'éval ne sera pas celui qu'on nous a donné (testé sur littéralement toutes les données disponibles).<br>
1.3: Ajout d'une représentation visuelle des différentes actions et de l'argent de notre bot par dessus et décision d'utiliser la stratégie 1 suite aux tests précédents (version actuelle et finale).<br>

## Comment l'installer et l'utiliser?
Pour cette section, nous allons assumer que vous savez utiliser un ordinateur mais ne savez rien de la programmation. Si c'est le cas et que vous vous retrouvez bloqués, [contactez-nous](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md#nous-contacter).

First, you're gonna need python. For this part, check [my tutorial on how to do so](https://github.com/reza0310/Tutorials/blob/python/README.en.md).<br>
Congratulations! You now have Python!

Next step is to install the parent project. Download our [teacher's repository](https://github.com/benjaminforest/beagleboys). For those of you who think it's a little bit too much just to launch an object, note that it was designed to make a bunch of bots like ours compete.<br>
Congratulations! You now have the parent project!

The final step is to install the child project wich is ours. First download it as ZIP like you did for the last one from [this link](https://github.com/reza0310/ProjetTradingPythonPOO) (wich might be the link you're coming from). Then extract it into the parent project's folder. If it asks you if you want to replace files, approve.<br>
Congratulations! You just finished the installation!

Now, to use it, check the [file-by-file description](https://github.com/reza0310/ProjetTradingPythonPOO#file-by-file-description) to know wich script to execute and why.

## Description fichier par fichier
- [.gitignore](https://github.com/benjaminforest/beagleboys/blob/main/.gitignore): File listing the files and folders the author don't want to upload to github.
- [.gitmodules](https://github.com/benjaminforest/beagleboys/blob/main/.gitmodules): Links to other student's projects for them to appear on our teacher's repository.
- [README.md](https://github.com/benjaminforest/beagleboys/blob/main/README.md): Informations for us students.
- [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py): A simple example bot made by our teacher for demonstration purpose (wich our bot inherit from just for the line 9 and the challenge XD)
- [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py): Client used by our bots to buy and sell stakes and to verify we don't cheat. Also give us informations about how much money and actions we have.
- [candle_sample.txt](https://github.com/benjaminforest/beagleboys/blob/main/candle_sample.txt): Just some example data for us to test our bots on.
- [collect_candles.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles.py): Executable but slow and not quite up-to-date. An old script to make candle_sample files.
- [collect_candles2.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles2.py): Executable. The actual script to make candle_sample files. Lines 10 and 13 are from starting and ending datetimes to collect data between. The API allow us to collect data month by month from today to a year before.
- [collect_data.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_data.py): Executable but useless. Yet another try at collecting condles. If you run into errors, check that you installed [the right module](https://stackoverflow.com/questions/42905748/i-am-getting-attribute-error-module-object-has-no-attribute-enabletrace-whi). It only save collected data every 100 candle and don't get close prices.
- [gui.py](https://github.com/benjaminforest/beagleboys/blob/main/gui.py): Executable but useless. An exemple graphical interface to help students who need it to achieve their own.
- [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py): EXECUTABLE. The core program. Linking every one of our bots to a [botorderclient](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py) and using [shared's folder shared.py script](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py) for basically everything.
- [main_simple.py](https://github.com/benjaminforest/beagleboys/blob/main/main_simple.py): A simpler version of main.py. Might be executable if the [parent project's author](https://github.com/benjaminforest) accept [pull request #4](https://github.com/benjaminforest/beagleboys/pull/4).
- FOLDER: shared (A folder containing main.py's important code)
    - [\_\_init__.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/__init__.py): Empty file. (May not exist anymore if [our teacher](https://github.com/benjaminforest) accept [pull request #3](https://github.com/benjaminforest/beagleboys/pull/3)).
    - [shared.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py): Functions being basically the whole code of [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py).
- FOLDER: ProjetTradingPythonPOO (My team's project)
    - [.gitignore](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/.gitignore): File listing the files and folders the author don't want to upload to github.
    - [LICENSE](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE): A file expliciting your rights and duties about the project.
    - [README.en.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md): A file in english explaining everything about the project. This very file you are actually reading.
    - [README.fr.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.fr.md): A file in french explaining everything about the project.
    - [README.md](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.md): A file linking all languages README files.
    - [bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py): My team's bot. Can't be called directly. Inherit from [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py) to get self.client wich is an instance from [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py). Uses [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) to communicate with [ProjetTradingPythonPOO/graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py).
    - [collect_candles.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/collect_candles.py): My own try at making the [collect_candle.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles.py) file based on our teacher's description while he was making it himself.
    - [globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py): A small file to define some ultra-global variables to make [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) and [ProjetTradingPythonPOO/graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py) communicate.
    - [graph.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/graph.py): EXECUTABLE. Uses [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) to inform [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) (who inherit from [beaglebot.py](https://github.com/benjaminforest/beagleboys/blob/main/beaglebot.py)) to collect data while executing (by using the "affichage" boolean). Then make a copy of [candle_sample.txt](https://github.com/benjaminforest/beagleboys/blob/main/candle_sample.txt) at ProjetTradingPythonPOO/candle_sample.txt before executing [main.py](https://github.com/benjaminforest/beagleboys/blob/main/main.py) (who uses [shared/shared.py](https://github.com/benjaminforest/beagleboys/blob/main/shared/shared.py) and connect bots to [botorderclient.py](https://github.com/benjaminforest/beagleboys/blob/main/botorderclient.py)) for [ProjetTradingPythonPOO/bot.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/bot.py) to collect data about candles and, moreover, about himself. After this crucial execution, this script ask [ProjetTradingPythonPOO/globals.py](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/globals.py) for the data and set up a cool display for each symbol showing this symbol's variations and our bot's money over the time. I know there's a lot of files involved but basically that's the script you are looking for if you just wanna see cool results XD.
    - [A_year_worth_of_data.zip](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/A_year_worth_of_data.zip): File made with twelve uses of the [collect_candles2.py](https://github.com/benjaminforest/beagleboys/blob/main/collect_candles2.py) script on the 14/02/2022 for archiving and API capacities bypassing purposes. Contains probably all data from 14/02/2021 to 14/02/2022.
- All of the remaining folders are other student's projects wich I didn't studied so I can't say a lot about these.

## Comment contribuer?
Sachant qu'il s'agit d'un projet scolaire, seuls les camarades de mon groupe de travail son autorisés à participer. Si vous avez vraiment très envie de modifier des choses je ne peux que vous conseiller de faire une fork et si vous voulez que je publie vos modifications pour une raison ou pour une autre [venez en discuter avec moi](https://github.com/reza0310/ProjetTradingPythonPOO#contact-us).
Malgré celà, vous pouvez quand même nous aider en ouvrant des rapports de problèmes (bugs, demandes, ...) sur la [page dédiée](https://github.com/reza0310/ProjetTradingPythonPOO/issues)! Si vous le faites, merco beaucoup!

## FAQ
Aucune question ne nous a encore été posée.

## Nous contacter
reza0310: [page de contact](https://github.com/reza0310#a-propos-de-mon-profil).

## License
Lisez le [fichier "LICENSE"](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE) (en anglais).

### Dernière mise à jour de la documentation 
Mardi 1 mars 2022
