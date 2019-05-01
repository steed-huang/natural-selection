"""Natural Selection Creature Survival Simulation"""
import sys
import math
import random
import os
import pygame
import creature
import projectile
import world
import food


pygame.init()

WIN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Natural Selection")

RUN = True

while RUN:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    WIN.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
