import pygame
import config

class HumanAgent:

    def decision(self, pac, ghosts, grid):
        return pygame.key.get_pressed()

class SmartAgent:

    def __init__(self, network):

        self.net = network

    def decision(self, pac, ghosts, grid):

        entries = [
            pac.grid_pos[0],
            pac.grid_pos[1],
            pac.way,
            pac.direction
        ]

        out = self.net.activate(entries)

        list = [
            (pygame.K_UP,       out[0]),
            (pygame.K_DOWN,     out[1]),
            (pygame.K_LEFT,     out[2]),
            (pygame.K_RIGHT,    out[3]),
        ]

        list.sort(key=lambda x: x[1], reverse=True)

        keys = { x[0]: False for x in list }
        keys[list[0][0]] = True

        return keys
