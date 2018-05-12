import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, grid_pos, speed, way, direction):
        super().__init__(self)

        self.screen_pos = (grid_pos[0]*globals.TILE_SIZE, grid_pos[1]*globals.TILE_SIZE)

        self.grid_pos = grid_pos
        self.speed = speed
        self.way = way

        self.rect = pygame.Rect((self.screen_pos[0], self.screen_pos[1],
                                 globals.TILE_SIZE, globals.TILE_SIZE))

    def move(self):

        if self.direction = globals.X_DIRECTION:

            if self.way = globals.PLUS_WAY:

                self.rect.x += 1
                self.screen_pos[0] += 1

            else:

                self.rect.x -= 1
                self.screen_pos[0] -= 1

        else:

            if self.way = globals.PLUS_WAY:

                self.rect.y += 1
                self.screen_pos[1] += 1

            else:

                self.rect.y -= 1
                self.screen_pos[1] -= 1
