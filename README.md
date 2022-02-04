# Python Trading Bot Project

## Why?
This project is actually a school project. Our objective is to make a bot able to make the maximum of money from some data. Data comes from "https://finnhub.io/docs/api/stock-candles". It is not intended for use on real markets nor anything like that don't try to make money out of it you risk losing it all.

## Versions
0.0: In development (not working) (actual version)

## How to install and use it?
For this section, we will assume that you know how to use a computer but know nothing about programming. 

First, you're gonna need python. Download it from the [official website](https://www.python.org/downloads/). During python's installations you will have a checkbox for if you want to asked Python to PATH. Do it. Then you will be asked if you want to disable PATH length limit. Do it. 
Congratulations! You now have Python!

Next step is to install the parent project. Download our [teacher's repository](https://github.com/benjaminforest/beagleboys). Once you are on the website click the green "Code" button then "Download ZIP". Extract it anywhere you want. For those of you who understand this file you might think it's a little to much just to launch an object but it was designed to make a bunch of bots like ours compete. The problem is that even with these files some edits will be needed. If you have your own app to edit them then you're on your own. If not, download notepad++ from [their website](https://notepad-plus-plus.org/downloads/) then right click on the files you need to edit and click "Edit with notepad++". The changes you will have to make are the following:
-Replace line 2 with `import os` (for optimisation purposes)
-Replace lines 3 and 4 with `sys.path.append(os.path.join(os.path.dirname(__file__), 'ProjetTradingPythonPOO'))`
-Replace the line wich is now line 5 with `from bot import Bot`
-Replace the line wich is now line 7 with `robot1 = Bot()`
Congratulations! You now have the parent project!

The final step is to install the child project. First download it as ZIP like you did for the last one from [this link](https://github.com/reza0310/ProjetTradingPythonPOO) (wich might be the link you're actually on). Then extract it into the parent project's folder. You should now have a new folder into the parent folder.
Congratulations! You just finished the installation!

Now, to use it, you will only need to double-click the "main.py" file in the parent project's directory.

## How to contribute
Since this is a school project, only invited contributors wich are in fact classmates working in my group are allowed to contribute. If you really want to modify things up you can fork this repository and if you want me to publish it for some reasons contact me with the contact informations down below.

## FAQ
No questions were asked to us for now.

## Contact us
reza0310:
  e-mail: reza031077@yahoo.fr (response time: I might even never answer but I will say between a week and a year)
  discord: reza0310#0310 (response time: A day)

## License


### Last updated Wednesday 4th February 2022
