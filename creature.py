"""creature class module"""
import random
import pygame
import pg
import genome
from food import Food


class Creature():
    """creature has different attributes based off its genes"""
    img1 = pygame.image.load('assets/creature.png')
    img2 = pygame.image.load('assets/mating_creature.png')

    def __init__(self, x, y):
        self.gene = genome.Genome()
        self.x_pos = x
        self.y_pos = y
        self.rad = 10
        self.health = 30 + 30 * ((20 * self.gene.dna[0]) / 100)
        self.damage = 10 + 10 * ((20 * self.gene.dna[1]) / 100)
        self.speed = 0.5 + 0.5 * ((20 * self.gene.dna[2]) / 100)
        self.vision = 80 + 80 * ((20 * self.gene.dna[3]) / 100)
        self.aggro = 20 + 20 * ((20 * self.gene.dna[4]) / 100)
        self.satiation = 0
        self.last_starve = 0
        self.hunger = 8000 - 1000 * self.speed - 6 * self.vision
        self.c_img = pygame.transform.scale(
            self.img1, (self.rad*2, self.rad*2))
        self.mc_img = pygame.transform.scale(
            self.img2, (self.rad*2, self.rad*2))

    def move(self):
        """moves creature"""
        # breeding
        other_move = False
        if self.satiation >= 3:
            for ctr in pg.CREATURES:
                if ctr != self and ctr.satiation >= 3 and pg.distance((self.x_pos, self.y_pos), (ctr.x_pos, ctr.y_pos)) <= self.vision:
                    self.move_towards(ctr.x_pos, ctr.y_pos)
                    other_move = True
                    if pg.distance((self.x_pos, self.y_pos), (ctr.x_pos, ctr.y_pos)) < self.rad * 2:
                        self.satiation = 2
                        ctr.satiation = 2
                        pg.CREATURES.append(
                            self.reproduce(self.x_pos, self.y_pos,
                                           self.gene.dna, ctr.gene.dna))
        # eating
        if not other_move:
            closest = Food(9999, 9999)
            for apple in pg.FOOD:
                if pg.distance((self.x_pos, self.y_pos), (apple.x_pos, apple.y_pos)) < pg.distance((self.x_pos, self.y_pos), (closest.x_pos, closest.y_pos)):
                    closest = apple
            if pg.distance((self.x_pos, self.y_pos), (closest.x_pos, closest.y_pos)) <= self.vision:
                self.move_towards(closest.x_pos, closest.y_pos)
                other_move = True
                if pg.distance((self.x_pos, self.y_pos), (closest.x_pos, closest.y_pos)) < closest.rad * 2:
                    pg.FOOD.pop(pg.FOOD.index(closest))
                    self.eat()
        # random jiggle movement
        if not other_move:
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

    def move_towards(self, x_pos, y_pos):
        """moves creature towards given pair of coordinates"""
        if self.x_pos < x_pos:
            self.x_pos += self.speed
        else:
            self.x_pos -= self.speed
        if self.y_pos < y_pos:
            self.y_pos += self.speed
        else:
            self.y_pos -= self.speed

    def eat(self):
        """increases satiation after eating"""
        self.satiation += 1

    def starve(self, time):
        """uses up satiation every 'hunger' seconds, dies if no satiation"""
        if self.last_starve == 0:
            self.last_starve = time
        elif time - self.last_starve >= self.hunger:
            self.satiation -= 1
            self.last_starve = time
        if self.satiation < 0:
            pg.CREATURES.pop(pg.CREATURES.index(self))

    def reproduce(self, x_pos, y_pos, dna1, dna2):
        """creates new child creature"""
        new_creature = type(self)(x_pos, y_pos)
        new_creature.gene.combine(dna1, dna2)
        new_creature.gene.mutate()
        new_creature.update_atts()
        return new_creature

    def update_atts(self):
        """updates attributes to be affected by genes"""
        self.health = 30 + 30 * ((10 * self.gene.dna[0]) / 100)
        self.damage = 10 + 10 * ((10 * self.gene.dna[1]) / 100)
        self.speed = 0.5 + 0.5 * ((10 * self.gene.dna[2]) / 100)
        self.vision = 80 + 80 * ((10 * self.gene.dna[3]) / 100)
        self.aggro = 20 + 20 * ((10 * self.gene.dna[4]) / 100)
        self.hunger = 8000 - 1000 * self.speed - 6 * self.vision

    def draw(self):
        """draws creature"""
        if self.satiation >= 3:
            pg.WIN.blit(self.mc_img, (self.x_pos-self.rad,
                                      self.y_pos-self.rad))
        else:
            pg.WIN.blit(self.c_img, (self.x_pos-self.rad,
                                     self.y_pos-self.rad))
        # shows vision (for debug)
        # pygame.draw.circle(pg.WIN, (255, 0, 0),
        #                   (round(self.x_pos), round(self.y_pos)), round(self.vision), 1)
