import pygame
import character
import globals
import config

# states
CHASE       = 0
FRIGHTENED  = 1
SCATTER     = 2

class Ghost(character.Character):

    state = CHASE

    sprites = globals.GHOSTS_SPRITES[0]
    frightened_sprites = globals.GHOSTS_SPRITES[4]
    current = 0

    def __init__(self, grid_pos, way, direction, home):
        super().__init__(grid_pos, 4, way, direction)

        self.home = home

    def euclidians_distance(self, a, b):
        return ( (b[0]-a[0])**2 + (b[1]-a[1])**2 )**(1/2)

    def update_way(self, grid):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]] >> 3

        flags &= ~(1 << ((self.direction << 1) + ((self.way+1)%2))) # proibe o fantasma de voltar

        if flags == globals.UP:

            self.way = 0
            self.direction = 1

        elif flags == globals.DOWN:

            self.way = 1
            self.direction = 1

        elif flags == globals.RIGHT:

            self.way = 1
            self.direction = 0

        elif flags == globals.LEFT:

            self.way = 0
            self.direction = 0

        elif ((self.screen_pos[0]%config.TILE_SIZE == 0) and (self.screen_pos[1]%config.TILE_SIZE == 0)):

            dist = float('inf')

            if flags & globals.DOWN:
                point = (self.grid_pos[0], self.grid_pos[1] + 1)

                d = self.euclidians_distance(point, self.target)

                if d < dist:
                    dist = d
                    self.direction = 1
                    self.way = 1

            if flags & globals.UP:
                point = (self.grid_pos[0], self.grid_pos[1] - 1)

                d = self.euclidians_distance(point, self.target)

                if d < dist:

                    dist = d
                    self.direction = 1
                    self.way = 0

            if flags & globals.RIGHT:
                point = (self.grid_pos[0] + 1, self.grid_pos[1])

                d = self.euclidians_distance(point, self.target)

                if d < dist:

                    dist = d
                    self.way = 1
                    self.direction = 0

            if flags & globals.LEFT:
                point = (self.grid_pos[0] - 1, self.grid_pos[1])

                d = self.euclidians_distance(point, self.target)

                if d < dist:

                    dist = d
                    self.way = 0
                    self.direction = 0

    def update(self, screen, grid):

        self.move()
        self.update_way(grid)

        if self.state == FRIGHTENED:

            screen.blit(self.frightened_sprites[self.current], self.rect)

        else:

            screen.blit(self.sprites[self.direction][self.way][self.current], self.rect)

        self.current = (self.current + 1 ) % 2

class Blinky(Ghost):
    pass

class Pinky(Ghost):
    pass

class Inky(Ghost):
    pass

class Clyde(Ghost):
    pass
