"""Natural Selection Creature Survival Simulation"""
import random
import pygame
import pg
import creature
import food


def spawn(num):
    """spawns num creatures"""
    for _ in range(num):
        x_pos = random.randrange(100, 600)
        y_pos = random.randrange(100, 600)
        pg.CREATURES.append(creature.Creature(x_pos, y_pos))


def spawn_food(num):
    """spawns num food in random locations"""
    for _ in range(num):
        x_pos = random.randrange(700)
        y_pos = random.randrange(700)
        pg.FOOD.append(food.Food(x_pos, y_pos))


def creature_action(time):
    """carries out all creature processes"""
    for ctr in pg.CREATURES:
        ctr.move()
        ctr.starve(time)


def refill_food(num, refill_delay, time):
    """spawns in num food in refill_delay increments"""
    if time - pg.LAST_SPAWN >= refill_delay:
        pg.FOOD = []
        spawn_food(num)
        pg.LAST_SPAWN = time


def redraw():
    """redraws entire game"""
    pg.WIN.fill((0, 0, 0))
    for apple in pg.FOOD:
        apple.draw()
    for ctr in pg.CREATURES:
        ctr.draw()
    pygame.display.update()


spawn(10)
spawn_food(300)
RUN = True

while RUN:
    TIME = pygame.time.get_ticks()
    pygame.time.wait(5)  # uses less cpu than delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    refill_food(50, 10000, TIME)
    creature_action(TIME)
    redraw()


pygame.quit()
