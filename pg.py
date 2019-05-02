"""module for initializing shared pygame variables etc."""
import pygame

pygame.init()

WIN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Natural Selection")

CREATURES = []
