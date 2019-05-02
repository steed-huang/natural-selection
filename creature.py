"""creature class module"""
import random
import pygame
import pg
import genome


class Creature():
    """creature has different attributes based off its genes"""
    img = pygame.image.load('assets/creature.png')

    def __init__(self, x, y):
        self.gene = genome.Genome()
        self.x_pos = x
        self.y_pos = y
        self.rad = 10
        self.health = 30 + 30 * ((10 * self.gene.genetic_code[0]) / 100)
        self.damage = 10 + 10 * ((10 * self.gene.genetic_code[1]) / 100)
        self.speed = 1 + 1 * ((10 * self.gene.genetic_code[2]) / 100)
        self.vision = 30 + 30 * ((10 * self.gene.genetic_code[3]) / 100)
        self.aggro = 20 + 20 * ((10 * self.gene.genetic_code[4]) / 100)

        self.satiation = 0
        self.c_img = pygame.transform.scale(self.img, (self.rad*2, self.rad*2))

    def move(self):
        """moves creature"""
        rand = random.randrange(4)
        if rand == 0:
            if self.x_pos + self.rad + self.speed < 700:
                self.x_pos += self.speed
        if rand == 1:
            if self.x_pos - self.rad - self.speed > 0:
                self.x_pos -= self.speed
        if rand == 2:
            if self.y_pos + self.rad + self.speed < 700:
                self.y_pos += self.speed
        if rand == 3:
            if self.y_pos - self.rad - self.speed > 0:
                self.y_pos -= self.speed

    def eat(self):
        """increases satiation after eating"""
        self.satiation += 1

    def draw(self):
        """draws creature"""
        pg.WIN.blit(self.c_img, (self.x_pos-self.rad, self.y_pos-self.rad))
        # vision indicator
        # pygame.draw.circle(pg.WIN, (255, 0, 0), (self.x_pos, self.y_pos), self.vision, 1)
