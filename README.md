Welcome to Mario!
===================
*Coded by:*
**Arnav Juneja**

This **README** file contains :
 1. Information About the Game
 2. Controls
 3. Description of Classes Created
 4. Instructions on how to Run the Code
 5. Requirements
----------


About The Game
-------------
Mario (Japanese: マリオ Hepburn: Mario, [ma.ɾi.o]) (English: /ˈmɑːrioʊ, ˈmær-/; Italian: [ˈmaːrjo]) is a fictional character in the Mario video game franchise, owned by Nintendo and created by Japanese video game designer Shigeru Miyamoto. Serving as the company's mascot and the eponymous protagonist of the series, Mario has appeared in over 200 video games since his creation. Depicted as a short, pudgy, Italian plumber who resides in the Mushroom Kingdom, his adventures generally center upon rescuing Princess Peach from the Koopa villain Bowser. His younger brother and sidekick is Luigi. 
For more ,refer : https://en.wikipedia.org/wiki/Mario

----------


Controls
-------------------

> w - move up
> d - move right
> a - move left
> i - cheat to increase lives
------------------------

Description of Classes Created
--------------------------------------------
####Board:
The board class creates a 42x80 board for gameplay, with boundaries, walls and empty spaces. It also comprises of a getprint function to take a print of the board.
####Mario:
The Mario class has all the variables and functionality of Bomberman, this includes the generation and movement . This inherits Boss.
####Boss:
The Boss class does not inherit any other class, it creates a boss. It comprises of getprint and printbullets function to print it and its bullets on board, moveboss and movebullets to move boss and its bullets and kill boss to finally kill it
####Enemy:
The Enemy class inherits no other functions, and adds 5 enemies to the board, it manages the motion, deletion, generation and functionality of enemies.
####Manage:
Manage class manages score, printing, and the killing of Bomberman.

__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 run.py
```
>- press 'q' to quit.

___________________

Reqiurements:
--------------------
- written seperately in requirements.txt file
_______________

###Arnav Juneja
####20161071