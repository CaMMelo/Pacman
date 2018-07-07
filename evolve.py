#!/usr/bin/python

import neat
import agent
import pygame
import app
import time
import pickle

def pop_fitness(genomes, config):

    for id, genome in genomes:

        genome.fitness = fitness(genome, config)

def fitness(genome, config):

    # calculate the fitness of a genome
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    brain = agent.SmartAgent(net)

    game = app.PacmanApp(brain)

    game.run()

    return game.game.pacman.distance

def run(cfgfile):

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, cfgfile)

    p = neat.Population(config)
    # irá carregar a ultima geração execuda
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-?')

    # reporter to see outputs on stdout
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(100))

    # executa 3000 gerações
    # pe = neat.ParallelEvaluator(2, fitness)
    winner = p.run(pop_fitness, 3000)

    return winner # retorna o resultado do treinamento


if __name__ == '__main__':
    result = run('neat_configuration')

    with open('output.net', 'wb+') as ostream:
        result = pickle.dumps(result)
        ostream.write(result)
