# Heart Attack
## CS 180 MP

## Overview:
Our project, entitled "Heart Attack" is a Tower Defense game that features a
specialized AI used to generate an optimized sequence of enemies that can be
produced given a limited amount of ATP provided for a certain arrangement of
towers present on the grid. The main objective of the enemy AI is to eliminate
the player, by attacking its 'heart' at the end of the grid, reducing its life points to zero.

## Requirements
1. Python 2.7 or greater
2. Pygame 1.9.1

## Files
1. main.py - Contains the main game logic
2. genetic.py - Contains genetic algorithm for training the AI
3. classes - Contains classes used by the game logic
a. AI.py - Basic AI algorithms used in the game
b. ATP.py - Sprite of ATP plus holds information about ATP of player and virus
c. base.py - Contains base classes
d. bullet.py - Contains bullet logic and sprite
e. DS.py	- Contains datastructes used
f. member.py - Contains member class used by genetic, contains imformation
	multipliers
g. thing.py		- Contains heart sprite and logic
h. tower.py 	- Contains tower base, sprites, information, and logic
i. towerAI.py		- Contains AI for tower
j. trivia.py	- Contains trivias and its sprites
k. UI.py 	- Contains UI like popup
l. virus.py	- Contains virus base, information, and sprite. Also includes virus groups
m. virusAI.py - Contains AI for virus
4. ai - Contains multipliers to be used by the game by default

## Running
To run the game
```
python main.py
```

To run the game and save your actions
```
python main.py -r <actionfile>
```

To run the game and let an AI place the tower according to your recorded actionfile
```
python main.py -a <actionfile>
```

To run the game with custom multipliers
```
python main.py -v <datafile>
```

To train the ai (note: this excepts a file named actions in the base directory)
```
python genetic.py
```

## Training
In training the AI, the genetic algorithm will generate the population composed of different members.
A member is a set of multipliers to be used by the game to determine what proportion of virus is to be released
based on the towers the defender has and the current wave. Each member is to be evaluated by applying 
that set of multipliers to a game and getting the fitness of it. The fitness of a member is defined to be the damage
done to the heart / wave it took to kill it or 15(it stops after 15 waves if its training). After that, two members are 
randomly selected then the one with lower fitness is dropped while the fitter one is saved for crossover. This is done
until only have of the population remains. The remaining members are randomly crossed-over with 1% chance
of their offspring being mutated. Cycle repeats, the final population is then saved at ./ai/data.net
