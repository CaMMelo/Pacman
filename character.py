import pygame
import config
import globals

class Character(pygame.sprite.Sprite):

    def __init__(self, grid_pos, speed, way, direction):
        pygame.sprite.Sprite.__init__(self)

        self.screen_pos = (grid_pos[0]*config.TILE_SIZE, grid_pos[1]*config.TILE_SIZE)

        self.grid_pos   = grid_pos
        self.speed      = speed
        self.way        = way
        self.direction  = direction

        self.rect = pygame.Rect((self.screen_pos[0], self.screen_pos[1],
                                 config.TILE_SIZE, config.TILE_SIZE))

    def move(self):

        if self.direction == globals.Y_DIRECTION:
            if self.way == globals.PLUS_WAY:
                self.rect.y += self.speed
                self.screen_pos = (self.screen_pos[0], self.screen_pos[1] + self.speed)
            else:
                self.rect.y -= self.speed
                self.screen_pos = (self.screen_pos[0], self.screen_pos[1] - self.speed)
        else:
            if self.way == globals.PLUS_WAY:
                self.rect.x += self.speed
                self.screen_pos = (self.screen_pos[0] + self.speed, self.screen_pos[1])
            else:
                self.rect.x -= self.speed
                self.screen_pos = (self.screen_pos[0] - self.speed, self.screen_pos[1])

        if (self.screen_pos[0]%config.TILE_SIZE == 0) and (self.screen_pos[1]%config.TILE_SIZE == 0):
            self.grid_pos = (self.screen_pos[0]//config.TILE_SIZE, self.screen_pos[1]//config.TILE_SIZE)
