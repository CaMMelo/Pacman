import neat
import agent as agnt
import os
import pygame
import app

def eval_genome(genome, config):

    net = neat.nn.FeedForwardNetwork.create(genome, config)
    agent = agnt.SmartAgent(net)

    application = app.PacmanApp(agent)

    max = application.g.grid.pellet_count

    application.run()

    return application.g.pacman.score / max


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'neat_configuration')

p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

pe = neat.ParallelEvaluator(4, eval_genome)
winner = p.run(pe.evaluate, 5000)
