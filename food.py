"""food class module"""
import pygame


class Food():
    """food for creature consumption"""
    img = pygame.image.load('assets/apple.png')

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.rad = 5
        self.f_img = pygame.transform.scale(self.img, (self.rad*2, self.rad*2))

    def draw(self, WIN):
        """draws food"""
        WIN.blit(self.f_img, (self.x_pos-(self.rad), self.y_pos-(self.rad)))
