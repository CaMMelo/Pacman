import pygame
import config
import globals

def ang(a, b):
    ''' Cosseno do ponto b em relação ao ponto a '''

    hp = globals.euclidians_distance(a, b)
    ca = a[0] - b[0]
    if hp > 0:
        return ca/hp

    return 0

class HumanAgent:
    ''' Agente controlado pelas entradas do teclado '''

    def decision(self, pac, ghosts, grid):
        return pygame.key.get_pressed()

class SmartAgent:
    ''' Agente controlado por uma rede neural '''

    key_direction = {
        globals.UP     : pygame.K_UP,
        globals.DOWN   : pygame.K_DOWN,
        globals.LEFT   : pygame.K_LEFT,
        globals.RIGHT  : pygame.K_RIGHT,
    }

    def __init__(self, network):

        self.net = network

    def choose_keys(self, results, next, pac):
        ''' dado os resultados da rede, decide qual tecla precionar '''

        # A tecla com maior saída é escolhida

        results.sort(key=lambda x: x[1], reverse=True)

        keys = { x[0]: False for x in results }
        keys[results[0][0]] = True

        return keys

    def decision(self, pac, ghosts, grid):
        ''' executa a rede neural e retorna a direção escolhida '''

        ghosts_distances = [ # (ghost_id, distance, state, direction)
            (0, globals.euclidians_distance(pac.grid_pos, ghosts[0].grid_pos),
                ghosts[0].state, 1 << ((ghosts[0].direction << 1) | ghosts[0].state)),

            (1, globals.euclidians_distance(pac.grid_pos, ghosts[1].grid_pos),
                ghosts[1].state, 1 << ((ghosts[1].direction << 1) | ghosts[1].state)),

            (2, globals.euclidians_distance(pac.grid_pos, ghosts[2].grid_pos),
                ghosts[2].state, 1 << ((ghosts[2].direction << 1) | ghosts[2].state)),

            (3, globals.euclidians_distance(pac.grid_pos, ghosts[3].grid_pos),
                ghosts[3].state, 1 << ((ghosts[3].direction << 1) | ghosts[3].state))
        ]

        ghosts_distances.sort(key=lambda x: x[1])

        x, y = pac.grid_pos
        next = {
            pygame.K_UP      : 0 if (y < 0) else (grid.grid[y-1][x]),
            pygame.K_DOWN    : 0 if (y+1 >= config.GRID_SIZE[1]) else (grid.grid[y+1][x]),
            pygame.K_LEFT    : 0 if (x < 0) else (grid.grid[y][x-1]),
            pygame.K_RIGHT   : 0 if (x+1 >= config.GRID_SIZE[0]) else (grid.grid[y][x+1])
        }

        angles = [
            ang(ghosts[0].grid_pos, pac.grid_pos),
            ang(ghosts[1].grid_pos, pac.grid_pos),
            ang(ghosts[2].grid_pos, pac.grid_pos),
            ang(ghosts[3].grid_pos, pac.grid_pos),
        ]

        entries = [
            ghosts_distances[0][0], # ghost
            ghosts_distances[0][1], # distance
            ghosts_distances[0][2], # state
            ghosts_distances[0][3], # direction
            angles[ghosts_distances[0][0]], # angle

            ghosts_distances[1][0], # ghost
            ghosts_distances[1][1], # distance
            ghosts_distances[1][2], # state
            ghosts_distances[1][3], # direction
            angles[ghosts_distances[1][0]], # angle

            ghosts_distances[2][0], # ghost
            ghosts_distances[2][1], # distance
            ghosts_distances[2][2], # state
            ghosts_distances[2][3], # direction
            angles[ghosts_distances[2][0]], # angle

            ghosts_distances[3][0], # ghost
            ghosts_distances[3][1], # distance
            ghosts_distances[3][2], # state
            ghosts_distances[3][3], # direction
            angles[ghosts_distances[3][0]], # angle

            # around pacman
            next[pygame.K_UP],
            next[pygame.K_DOWN],
            next[pygame.K_RIGHT],
            next[pygame.K_LEFT],

            # pacman direction
            1 << ((pac.direction << 1) | (pac.way)),

            # how many pellets on the grid
            grid.pcount
        ]

        results = self.net.activate(entries)
        results = [
            (pygame.K_DOWN,     results[0]),
            (pygame.K_UP,       results[1]),
            (pygame.K_RIGHT,    results[2]),
            (pygame.K_LEFT,     results[3]),
        ]

        return self.choose_keys(results, next, pac)
