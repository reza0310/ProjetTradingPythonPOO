# Python Trading Bot Project

## Index
- [Why?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#why)
- [Versions](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#versions)
- [How to install and use it?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#how-to-install-and-use-it)
- [File-by-file description](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#file-by-file-description)
- [How to contribute?](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#how-to-contribute)
- [FAQ](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#faq)
- [Contact us](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#contact-us)
- [License](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#license)
- [Last README update](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#last-updated)

## Why?
This project is actually a school project. Our objective is to make a bot able to make the maximum of money from some data. Data comes from "https://finnhub.io/docs/api/stock-candles". It is not intended for use on real markets nor anything like that don't try to make money out of it you risk losing it all.

## Versions
0.0: In development (not working)<br>
1.1: First working version with only two strategies<br>
1.2: Added a third and a fourth strategy and tried on some more data to test our strategies' ability to adapt to different situations<br>
1.3: Added a visual representation and decided to use strategy one after version 1.2's researchs (actual version)<br>

## How to install and use it?
For this section, we will assume that you know how to use a computer but know nothing about programming. If you need any help, [contact us](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#contact-us).

First, you're gonna need python. For this part, check [my tutorial on how to do so](https://github.com/reza0310/Tutorials/blob/python/README.en.md).<br>
Congratulations! You now have Python!

Next step is to install the parent project. Download our [teacher's repository](https://github.com/benjaminforest/beagleboys) and unzip it anywhere. For those of you who think it's a little bit too much just to launch an object, note that it was designed to make a bunch of bots like ours compete.<br>
Congratulations! You now have the parent project!

The final step is to install the child project wich is ours. First download it as ZIP like you did for the last one from [this link](https://github.com/reza0310/ProjetTradingPythonPOO) (wich might be the link you're coming from). Then extract it into the parent project's folder. If it asks you if you want to replace files, approve.<br>
Congratulations! You just finished the installation!

Now, to use it, check the [file-by-file description](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#file-by-file-description) to know wich script to execute and why.

## File-by-file description
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

## How to contribute?
Since this is a school project, only invited contributors wich are in fact classmates working in my group are allowed to contribute. If you really want to modify things up you can fork this repository and if you want me to publish it for some reasons contact me with the [contact informations](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/README.en.md#contact-us) down below.
Yet you can still help us by opening issues on the [issue page](https://github.com/reza0310/ProjetTradingPythonPOO/issues)! If you do so, thanks!

## FAQ
No questions were asked to us for now.

## Contact us
reza0310: [contact page](https://github.com/reza0310#a-propos-de-mon-profil).

## License
See the ["LICENSE" file](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE).

### Last updated 
Tuesday 1st March 2022
