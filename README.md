# Wanderer app home assignment for IBS and Greenfox examination
## Parts of the project:
The project contains seven .py files (area, hero, enemies, cell, grid, tábla and resource) and a map for the eight gif files used in the project
#### Resource
This file handles the gifs used in the project, loading them when called by other classes 
#### Cell
This file creates the cells with the necessary attributes, which are the building blocks of the game area
#### Grid
This file orders the cells into a playable area with walls and floor areas, based on the attributes given (like how big the game area should be)
#### Hero
This file handles most of what the hero is capable of. These include: the stats of the hero, the position of the hero, the strike function of the hero and the level of the hero
#### Enemies
This file handles the monsters of the game (skeletons and the boss). It draws them, assigns their number and stats, and provides the key which is needed to level up to a random monster
#### Area
This file handles the monsters on different level of the game
#### Gamelogic
This file makes makes the game work, meaning it uses other files and classes and executes them. It also handles the movement of the hero, including the change of image based on which way the hero is headed and the fact that he is not able to go to tiles which are walls
## Launching the game
1 Install Pythton 3.x to your system (the game was witten using 3.9, so it is 
2. Clone the repository to your PC
3. Open the directory that you pulled
4. Double click gamelogic.py
