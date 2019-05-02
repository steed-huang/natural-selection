"""gene class module"""
import random


class Genome():
    """genes assigned to each individual and changed upon breeding and mutation"""

    def __init__(self):
        self.genetic_code = {
            0: 0,  # health
            1: 0,  # damage
            2: 0,  # speed
            3: 0,  # vision
            4: 0  # aggro
        }

    def combine(self, gene1, gene2):
        """combines genes when bred"""
        for gene in gene1:  # should find some better combination method
            if random.randrange(2):  # 50% chance of passing on each genes
                self.genetic_code[gene] += gene1[gene]
        for gene in gene2:
            if random.randrange(2):  # 50% chance of passing on each genes
                self.genetic_code[gene] += gene2[gene]

    def mutate(self):
        """random chance of gene mutation"""
        rand = random.randint(1, 100)
        if rand <= 5:
            self.genetic_code[random.randrange(5)] += 1
        elif rand > 95:
            self.genetic_code[random.randrange(5)] -= 1
