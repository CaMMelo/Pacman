import pygame
import config
import globals

class Character(pygame.sprite.Sprite):

    scont = 0

    def __init__(self, grid_pos, speed, way, direction):
        pygame.sprite.Sprite.__init__(self)
        # self.speed = speed

        self.reset(grid_pos, speed, way, direction)

    def reset(self, grid_pos, speed, way, direction):

        self.grid_pos = grid_pos
        self.speed = speed
        self.scont = 0
        self.way = way
        self.direction = direction
        self.update_screen_pos()

    def update_screen_pos(self):

        self.screen_pos = (self.grid_pos[0]*config.TILE_SIZE, self.grid_pos[1]*config.TILE_SIZE)
        self.rect = pygame.Rect(self.screen_pos[0], self.screen_pos[1], config.TILE_SIZE, config.TILE_SIZE)

    def update_grid_pos(self):

        if (self.screen_pos[0]%config.TILE_SIZE == 0) and (self.screen_pos[1]%config.TILE_SIZE == 0):
            self.grid_pos = (self.screen_pos[0]//config.TILE_SIZE, self.screen_pos[1]//config.TILE_SIZE)

    def move(self):

        mv = self.speed

        if self.scont + mv > config.TILE_SIZE:

            mv = config.TILE_SIZE - self.scont
            self.scont = 0

        else:

            self.scont += mv

        if self.direction == globals.Y_DIRECTION:
            if self.way == globals.PLUS_WAY:
                self.rect.y += mv
                self.screen_pos = (self.screen_pos[0], self.screen_pos[1] + mv)
            else:
                self.rect.y -= mv
                self.screen_pos = (self.screen_pos[0], self.screen_pos[1] - mv)
        else:
            if self.way == globals.PLUS_WAY:
                self.rect.x += mv
                self.screen_pos = (self.screen_pos[0] + mv, self.screen_pos[1])
            else:
                self.rect.x -= mv
                self.screen_pos = (self.screen_pos[0] - mv, self.screen_pos[1])

        # update grid_pos

        self.update_grid_pos()

        # teleport

        if self.grid_pos[0] < 0:
            self.grid_pos = (config.GRID_SIZE[0] - 1, self.grid_pos[1])
            self.update_screen_pos()

        elif self.grid_pos[0] >= config.GRID_SIZE[0] :

            self.grid_pos = (0, self.grid_pos[1])
            self.update_screen_pos()
