import pygame

import grid
import pacman
import ghost
import config
import globals

class Game:

    def __init__(self):

        self.grid = grid.Grid()
        self.pacman = ghost.Ghost((13, 26), 0, 0)

    def main(self, screen):

        running = True

        clock = pygame.time.Clock()

        while running:

            # clock.tick(25)

            keys = pygame.key.get_pressed()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:

                    running = False

            # if keys[pygame.K_DOWN]:
            #     self.pacman.update_way(self.grid.grid, globals.DOWN)
            # if keys[pygame.K_UP]:
            #     self.pacman.update_way(self.grid.grid, globals.UP)
            # if keys[pygame.K_RIGHT]:
            #     self.pacman.update_way(self.grid.grid, globals.RIGHT)
            # if keys[pygame.K_LEFT]:
            #     self.pacman.update_way(self.grid.grid, globals.LEFT)

            screen.fill((0,0,0,0))

            # self.pacman.consume_pellet(self.grid.grid)

            self.grid.draw_grid(screen)
            self.pacman.update(screen, self.grid.grid)

            pygame.display.flip()










if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode(config.SCREEN_SIZE)

    g = Game()
    g.main(screen)
