"""module for initializing shared pygame variables etc."""
import math
import pygame

pygame.init()

WIN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Natural Selection")

LAST_SPAWN = 0
LAST_PRINT = 0
CREATURES = []
FOOD = []


def distance(point1, point2):
    """distance formula function that takes two tuples"""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
