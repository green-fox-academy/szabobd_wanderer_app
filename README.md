# Wanderer app home assignment for IBS and Greenfox examination

## Parts of the project:
The project contains seven .py files (area, hero, enemies, cell, grid, gamelogic and resource) and a directory for the eight gif files used in the project (4 hero, 2 enemy, 2 tile)
1. Resource: This file handles the gifs used in the project, loading them when called by other classes
2. Cell: This file creates the cells with the necessary attributes, which are the building blocks of the game area
3. Grid: This file orders the cells into a playable area with walls and floor areas, based on the attributes given (like how big the game area should be)
4. Hero: This file handles most of what the hero is capable of. These include: the stats of the hero, the position of the hero, the strike function of the hero and the level of the hero
5. Enemies: This file handles the monsters of the game (skeletons and the boss). It draws them, assigns their number and stats, and provides the key which is needed to level up to a random monster
6. Area: This file handles the monsters on different level of the game
7. Gamelogic: This file makes makes the game work, meaning it uses other files and classes and executes them. It also handles the movement of the hero, including the change of image based on which way the hero is headed and the fact that he is not able to go to tiles which are walls


## Launching the game
1. Install Pythton 3.x to your system (the game was witten using 3.9)
2. Clone the repository to your PC
3. Open the directory that you pulled
4. Double click gamelogic.py

## Gameplay
When the game is running, the hero starts in the upper left corner of the maze. The hero needs to kill the boss and the skleton with the key to move on to the next level. The heros stats can be seen in the bottom, on a white rectangle. When on the same tile with an enemy, the stats of the enemy can be seen on this part as well.

## Controls
- To move around, use `wasd`: To move up, hit `w`, to move down, hit `s`, to move right, hit `d`, to move left, hit `a`
- When on the same cell with an enemy, use `space` to attack
  
  

