import pygame
import character
import globals


# states
CHASE       = 0
FRIGHTENED  = 1
SCATTER     = 2

class Ghost(character.Character):

    def __init__(self, grid_pos, speed, direction, state):
        super().__init__(self, grid_pos, speed, direction)

    def available_directions(self, grid):
        pass

    def update(self):
        pass

class Blinky(Ghost):
    pass

class Pinky(Ghost):
    pass

class Inky(Ghost):
    pass

class Clyde(Ghost):
    pass
