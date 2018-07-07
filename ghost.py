import pygame
import character
import globals
import config

from random import randint

# states

CHASE       = 5 # 18s
SCATTER     = 2 # 5s
FRIGHTENED  = 1 # 3s
DEFAULT = CHASE

class Ghost(character.Character):

    frightened_sprites = globals.GHOSTS_SPRITES[4]
    current = 0
    state = DEFAULT

    def __init__(self, grid_pos, way, direction, home):
        super().__init__(grid_pos, globals.FAST, way, direction)

        self.home = home

    def reset(self, grid_pos, speed, way, direction):
        super().reset(grid_pos, speed, way, direction)
        self.state = DEFAULT

    def update_way(self, grid, chase_args):

        flags = grid[self.grid_pos[1]][self.grid_pos[0]] >> 3

        flags &= ~(1 << ((self.direction << 1) + ((self.way+1)%2))) # proibe o fantasma de voltar

        if ((self.screen_pos[0]%config.TILE_SIZE == 0) and (self.screen_pos[1]%config.TILE_SIZE == 0)):

            dist = float('inf')

            if self.state == SCATTER:
                self.target = self.home
            if self.state == FRIGHTENED:
                self.target = (randint(0, config.GRID_SIZE[0]), randint(0, config.GRID_SIZE[1]))
            if self.state == CHASE:
                self.target = self.chase(chase_args)

            x, y = self.grid_pos

            if flags & globals.DOWN:
                point = (x, y + 1)
                d = globals.euclidians_distance(point, self.target)

                if d < dist:
                    dist = d
                    self.way = 1
                    self.direction = 1

            if flags & globals.UP:
                point = (x, y - 1)
                d = globals.euclidians_distance(point, self.target)

                if d < dist:
                    dist = d
                    self.way = 0
                    self.direction = 1

            if flags & globals.RIGHT:
                point = (x + 1, y)
                d = globals.euclidians_distance(point, self.target)

                if d < dist:
                    dist = d
                    self.way = 1
                    self.direction = 0

            if flags & globals.LEFT:
                point = (x - 1, y)
                d = globals.euclidians_distance(point, self.target)

                if d < dist:
                    dist = d
                    self.way = 0
                    self.direction = 0

    def update(self, screen, grid, chase_args):

        self.update_way(grid, chase_args)
        self.move()

        if self.state == FRIGHTENED:
            screen.blit(self.frightened_sprites[self.current], self.rect)
        else:
            screen.blit(self.sprites[self.direction][self.way][self.current], self.rect)

        self.current = (self.current + 1 ) % 2


class Blinky(Ghost):

    sprites = globals.GHOSTS_SPRITES[0]

    def __init__(self, grid_pos, way, direction):
        super().__init__(grid_pos, way, direction, (config.GRID_SIZE[0], 0))

    def chase(self, chase_args):
        return chase_args[0]

class Pinky(Ghost):

    sprites = globals.GHOSTS_SPRITES[1]

    def __init__(self, grid_pos, way, direction):
        super().__init__(grid_pos, way, direction, (0, 0))

    def chase(self, chase_args):

        if self.direction == globals.Y_DIRECTION:

            if self.way == globals.PLUS_WAY:
                return (chase_args[0][0], chase_args[0][1] + 4)
            else:
                return (chase_args[0][0], chase_args[0][1] - 4)
        else:

            if self.way == globals.PLUS_WAY:
                return (chase_args[0][0] + 4, chase_args[0][1])
            else:
                return (chase_args[0][0] - 4, chase_args[0][1])

class Inky(Ghost):

    sprites = globals.GHOSTS_SPRITES[2]

    def __init__(self, grid_pos, way, direction):
        super().__init__(grid_pos, way, direction, config.GRID_SIZE)

    def chase(self, chase_args):

        pacman = chase_args[0]
        blinky = chase_args[1]

        return (blinky[0] + (pacman[0] - blinky[0])*2,
                blinky[1] + (pacman[1] - blinky[1])*2)

class Clyde(Ghost):

    sprites = globals.GHOSTS_SPRITES[3]

    def __init__(self, grid_pos, way, direction):
        super().__init__(grid_pos, way, direction, (0, config.GRID_SIZE[1]))

    def chase(self, chase_args):

        dist = globals.euclidians_distance(self.grid_pos, chase_args[0])

        if dist >= 8:
            return chase_args[0]
        else:
            return self.home
