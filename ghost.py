import pygame
import character
import globals


# states
CHASE       = 0
FRIGHTENED  = 1
SCATTER     = 2

class Ghost(character.Character):

    def __init__(self, grid_pos, speed, way, direction, state):
        super().__init__(self, grid_pos, speed, way)

    def available_ways(self, grid):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]]
        flags >>= 2

        flags &= 1 << (~self.way + self.direction << 1)

        return flags

    def update(self, screen):

        self.move()

class Blinky(Ghost):
    pass

class Pinky(Ghost):
    pass

class Inky(Ghost):
    pass

class Clyde(Ghost):
    pass
