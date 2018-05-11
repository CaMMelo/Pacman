import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, grid_pos, speed, direction):
        super().__init__(self)

        self.screen_pos = (grid_pos[0]*globals.TILE_SIZE, grid_pos[1]*globals.TILE_SIZE)
        self.grid_pos = grid_pos
        self.speed = speed
        self.direction = direction

        self.rect = pygame.Rect((self.screen_pos[0], self.screen_pos[1],
                                 globals.TILE_SIZE, globals.TILE_SIZE))
