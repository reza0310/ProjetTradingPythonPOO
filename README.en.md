# Python Trading Bot Project

## Index
- [Why?](https://github.com/reza0310/ProjetTradingPythonPOO#why)
- [Versions](https://github.com/reza0310/ProjetTradingPythonPOO#versions)
- [How to install and use it?](https://github.com/reza0310/ProjetTradingPythonPOO#how-to-install-and-use-it)
- [File-by-file description](https://github.com/reza0310/ProjetTradingPythonPOO#file-by-file-description)
- [How to contribute?](https://github.com/reza0310/ProjetTradingPythonPOO#how-to-contribute)
- [FAQ](https://github.com/reza0310/ProjetTradingPythonPOO#faq)
- [Contact us](https://github.com/reza0310/ProjetTradingPythonPOO#contact-us)
- [License](https://github.com/reza0310/ProjetTradingPythonPOO#license)
- [Last README update](https://github.com/reza0310/ProjetTradingPythonPOO#last-updated)

## Why?
This project is actually a school project. Our objective is to make a bot able to make the maximum of money from some data. Data comes from "https://finnhub.io/docs/api/stock-candles". It is not intended for use on real markets nor anything like that don't try to make money out of it you risk losing it all.

## Versions
0.0: In development (not working)
1.1: First working version with only two strategies
1.2: Added a third and a fourth strategy and tried on some more data to test our strategies' ability to adapt to different situations
1.3: Added a visual representation and decided to use strategy one after version 1.2's researchs (actual version)

## How to install and use it?
For this section, we will assume that you know how to use a computer but know nothing about programming. If you need any help, [contact us](https://github.com/reza0310/ProjetTradingPythonPOO#contact-us).

First, you're gonna need python. For this part, check [my tutorial on how to do so](https://github.com/reza0310/Tutorials/blob/python/README.en.md).<br>
Congratulations! You now have Python!

Next step is to install the parent project. Download our [teacher's repository](https://github.com/benjaminforest/beagleboys). For those of you who think it's a little bit too much just to launch an object, note that it was designed to make a bunch of bots like ours compete.<br>
Congratulations! You now have the parent project!

The final step is to install the child project wich is ours. First download it as ZIP like you did for the last one from [this link](https://github.com/reza0310/ProjetTradingPythonPOO) (wich might be the link you're coming from). Then extract it into the parent project's folder. If it asks you if you want to replace files, approve.<br>
Congratulations! You just finished the installation!

Now, to use it, check the [file-by-file description](https://github.com/reza0310/ProjetTradingPythonPOO#file-by-file-description) to know wich script to execute and why.

## File-by-file description
- .gitignore: File listing the files and folders the author don't want to upload to github.
- .gitmodules: Links to other student's projects for them to appear on our teacher's repository.
- README.md: Informations for us students.
- beaglebot.py: A simple example bot made by our teacher for demonstration purpose (wich our bot inherit from just for the line 9 and the challenge XD)
- botorderclient.py: Client used by our bots to buy and sell stakes and to verify we don't cheat. Also give us informations about how much money and actions we have.
- candle_sample.txt: Just some example data for us to test our bots on.
- collect_candles.py: An old script to make candle_sample files.
- collect_candles2.py: The actual script to make candle_sample files. Lines 10 and 13 are from starting and ending datetimes to collect data between. The API allow us to collect data month by month from today to a year before.
- collect_data.py: \[TODO]
- gui.py: \[TODO]
- main.py: \[TODO]
- main_simple.py: \[TODO]
- FOLDER: ProjetTradingPythonPOO
    - .gitignore: File listing the files and folders the author don't want to upload to github.
    - LICENSE: A file expliciting your rights and duties about the project.
    - README.en.md: A file in english explaining everything about the project.
    - README.fr.md: A file in french explaining everything about the project.
    - README.md: A file linking all languages README files.
    - bot.py: \[TODO]
    - collect_candles.py: \[TODO]
    - globals.py: \[TODO]
    - graph.py: \[TODO]
    - A_year_worth_of_data.zip: File made with twelve uses of the collect_candles2.py script on the 14/02/2022 for archiving and API capacities bypassing purposes. Contains probably all data from 14/02/2021 to 14/02/2022.
- FOLDER: shared
    - \_\_init__.py: Empty file.
    - shared.py: \[TODO]
- All of the remaining folders are other student's projects wich I didn't studied so I can't say a lot about these.

## How to contribute?
Since this is a school project, only invited contributors wich are in fact classmates working in my group are allowed to contribute. If you really want to modify things up you can fork this repository and if you want me to publish it for some reasons contact me with the [contact informations](https://github.com/reza0310/ProjetTradingPythonPOO#contact-us) down below.
Yet you can still help us by opening issues on the [issue page](https://github.com/reza0310/ProjetTradingPythonPOO/issues)! If you do so, thanks!

## FAQ
No questions were asked to us for now.

## Contact us
reza0310: [contact page](https://github.com/reza0310#a-propos-de-mon-profil).

## License
See the ["LICENSE" file](https://github.com/reza0310/ProjetTradingPythonPOO/blob/main/LICENSE).

### Last updated 
Sunday 20th February 2022
