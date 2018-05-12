import pygame
import character

class Pacman(character.Character):

    def __init__(self, grid_pos, screen_pos, way, direction):
        super().__init__(self, grid_pos, screen_pos, way, direction)

    def available_ways(self, grid):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]]
        flags >>= 2

        return flags

    def consume_pellet(self, grid):
        pass
