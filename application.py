import config
import pygame
import globals


class Pacman:

    def __init__(self):

        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)

    def run(self):

        pygame.mixer.pre_init()
        pygame.font.init()
        pygame.init()

        running = True:


        while running:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:

                    running = False


            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:

                running = False


            pygame.display.flip()
