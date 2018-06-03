import pygame
import agent
import game
import config

class PacmanApp:

    def __init__(self, pacman_agent=agent.HumanAgent()):
        self.pacman_agent = pacman_agent

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)

        self.g = game.Game(self.pacman_agent)

    def run(self):

        self.g.loop(self.screen)

if __name__ == '__main__':

    a = PacmanApp()
    a.run()
