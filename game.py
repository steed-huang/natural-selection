"""main game class module"""
import random
import pygame
import creature
import food


class Game():
    """game class that handles pygame and important variables"""

    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Natural Selection")

        self.LAST_SPAWN = 0
        self.LAST_PRINT = 0
        self.CREATURES = []
        self.FOOD = []

    def run(self):
        """main game loop"""
        self.spawn_creature(15)
        self.spawn_food(20)
        RUN = True
        while RUN:
            TIME = pygame.time.get_ticks()
            pygame.time.wait(1)  # uses less cpu than delay

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False

            self.print_data(5000, TIME)
            self.refill_food(20, 1000, TIME)
            self.creature_action(TIME)
            self.redraw()

        pygame.quit()

    def spawn_creature(self, num):
        """spawns num creatures"""
        for _ in range(num):
            x_pos = random.randrange(1, 700)
            y_pos = random.randrange(1, 700)
            self.CREATURES.append(creature.Creature(x_pos, y_pos))

    def spawn_food(self, num):
        """spawns num food in random locations"""
        for _ in range(num):
            x_pos = random.randrange(1, 700)
            y_pos = random.randrange(1, 700)
            self.FOOD.append(food.Food(x_pos, y_pos))

    def creature_action(self, time):
        """carries out all creature processes"""
        for ctr in self.CREATURES:
            ctr.move(self.CREATURES, self.FOOD, time)
            ctr.attack()
            ctr.starve(self.CREATURES, time)

    def refill_food(self, num, refill_delay, time):
        """spawns in num food in refill_delay increments"""
        if time - self.LAST_SPAWN >= refill_delay:
            # pg.FOOD = []
            self.spawn_food(num)
            self.LAST_SPAWN = time

    def print_data(self, delay, time):
        """prints average genome of population"""
        if time - self.LAST_PRINT >= delay:
            print(len(self.CREATURES))
            self.LAST_PRINT = time

    def redraw(self):
        """redraws entire game"""
        self.WIN.fill((0, 0, 0))
        for apple in self.FOOD:
            apple.draw(self.WIN)
        for ctr in self.CREATURES:
            ctr.draw(self.WIN)
        pygame.display.update()
