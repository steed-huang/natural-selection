"""creature class module"""
import random
import math
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
        self.health = 30 + 30 * ((10 * self.gene.dna[0]) / 100)
        self.damage = 10 + 10 * ((10 * self.gene.dna[1]) / 100)
        self.speed = 1 + ((10 * self.gene.dna[2]) / 100)
        self.vision = 50 + 30 * ((10 * self.gene.dna[3]) / 100)
        self.aggro = 20 + 20 * ((10 * self.gene.dna[4]) / 100)
        self.satiation = 0
        self.c_img = pygame.transform.scale(self.img, (self.rad*2, self.rad*2))
        # self.hitbox = (self.x_pos-self.rad, self.y_pos -
        #               self.rad, self.rad * 2, self.rad*2)

    def move(self):
        """moves creature"""
        # the creature can be conflicted and stuck inbetween multiple apples in vision (feature? jk fix pls)
        for apple in pg.FOOD:  # move towards food
            if pg.distance((self.x_pos, self.y_pos), (apple.x_pos, apple.y_pos)) <= self.vision:
                try:
                    (d_x, d_y) = ((apple.x_pos - self.x_pos)/math.sqrt((apple.x_pos - self.x_pos) ** 2 + (apple.y_pos - self.y_pos) ** 2),
                                  (apple.y_pos - self.y_pos)/math.sqrt((apple.y_pos - self.y_pos) ** 2 + (apple.x_pos - self.y_pos) ** 2))
                except ZeroDivisionError:
                    (d_x, d_y) = (0, 0)
                self.x_pos += d_x * self.speed
                self.y_pos += d_y * self.speed
                if pg.distance((self.x_pos, self.y_pos), (apple.x_pos, apple.y_pos)) < apple.rad * 2:
                    pg.FOOD.pop(pg.FOOD.index(apple))
                    self.eat()

        rand = random.randrange(4)  # random jiggle movement
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
        # shows vision (for debug)
        pygame.draw.circle(pg.WIN, (255, 0, 0),
                           (round(self.x_pos), round(self.y_pos)), round(self.vision), 1)
