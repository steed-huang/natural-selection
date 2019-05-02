"""creature class module"""
import random
import pygame
import pg


class Creature():
    """creature has different attributes that can mutate upon """
    img = pygame.image.load('assets/creature.png')

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.speed = 5
        self.rad = 15
        self.health = 100
        self.damage = 25
        self.c_img = pygame.transform.scale(self.img, (self.rad, self.rad))

    def mutate(self):
        """random chance of attribute mutation"""
        self.health = 1

    def move(self):
        """moves creature"""
        rand = random.randint(0, 3)
        if rand == 0:
            if self.x_pos + (self.rad // 2) + 2 < 700:
                self.x_pos += 1
        if rand == 1:
            if self.x_pos - (self.rad // 2) - 2 > 0:
                self.x_pos -= 1
        if rand == 2:
            if self.y_pos + (self.rad // 2) + 2 < 700:
                self.y_pos += 1
        if rand == 3:
            if self.y_pos - (self.rad // 2) - 2 > 0:
                self.y_pos -= 1

    def draw(self):
        """draws creature"""
        pg.WIN.blit(self.c_img, (self.x_pos-(self.rad // 2),
                                 self.y_pos-(self.rad // 2)))
