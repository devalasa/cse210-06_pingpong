# Pong

Pong is a multiplayer game, based on the sports arcade video game that has the same name. There are two players, Player one uses the "w" and "s" keyboards shortcuts to play the game, and Player two uses the "up" and "down" keyboard shortcuts. The players must try to hit the ball, and while both players can do this, the round will continue. However, when a player doesn't hit the ball, the rival wins a point and that round ends. There are fifteen rounds, and the game ends when the players reach the last round, and the player with the most points wins the game.

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 pong

```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```

root (project root folder)
+-- pong (source code for game)
+-- game (specific game classes)
+-- casting (various actor classes)
+-- directing (director and scene manager classes)
+-- scripting (various action classes)
+-- services (various service classes)
+-- **main**.py (entry point for program)
+-- constants.py (game constants)
+-- README.md (general info)

```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Ogboanoh Richard (ogb22001@byui.edu)
```
