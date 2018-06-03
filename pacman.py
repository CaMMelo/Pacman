import pygame
import character
import globals
import config

LIVES = 3

class Pacman(character.Character):

    lives = LIVES
    score = 0

    sprites = globals.PACMAN_SPRITES
    current = 0

    def __init__(self, grid_pos, way, direction):
        super().__init__(grid_pos, globals.FAST, way, direction)

    def consume_pellet(self, grid):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]] >> 1
        super = False

        if flags & globals.PELLET:

            self.score += 10

            if flags & globals.SPELLET:

                self.score += 40
                super = True

            grid[self.grid_pos[1]][self.grid_pos[0]] &= ~((globals.PELLET | globals.SPELLET) << 1)

        return super

    def update_way(self, grid, direction):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]] >> 3

        if (flags & direction) and ((self.screen_pos[0]%config.TILE_SIZE == 0) and (self.screen_pos[1]%config.TILE_SIZE == 0)):

            self.direction = 0
            self.way = 0

            if direction == globals.DOWN:

                self.direction = 1
                self.way = 1

            if direction == globals.UP:

                self.direction = 1

            if direction == globals.RIGHT:

                self.way = 1

    def update(self, screen, grid):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]] >> 3

        if flags & (1 << ((self.direction * 2) + self.way)):

            self.move()

        screen.blit(self.sprites[self.direction][self.way][self.current], self.rect)

        self.current = (self.current + 1) % 3
