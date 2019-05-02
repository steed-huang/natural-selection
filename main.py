"""Natural Selection Creature Survival Simulation"""
import sys
import math
import random
import os
import pygame

import pg
import creature
import food


def spawn(num):
    """spawns num creatures"""
    for _ in range(num):
        pg.CREATURES.append(creature.Creature(350, 350))


def move_creatures():
    """moves every creature"""
    for ctr in pg.CREATURES:
        ctr.move()


def redraw():
    """redraws entire game"""
    pg.WIN.fill((0, 0, 0))
    for ctr in pg.CREATURES:
        ctr.draw()
    pygame.display.update()


spawn(1)
RUN = True

while RUN:
    TIME = pygame.time.get_ticks()
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    move_creatures()
    redraw()


pygame.quit()
