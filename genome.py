"""gene class module"""
import random


class Genome():
    """genes assigned to each individual and changed upon breeding and mutation"""

    def __init__(self):
        self.dna = {
            0: 0,  # health
            1: 0,  # damage
            2: 0,  # speed
            3: 0,  # vision
            4: 0  # aggro
        }

    def combine(self, dna1, dna2):
        """combines genes when bred"""
        for gene in dna1:  # should find some better combination method
            self.dna[gene] += dna1[gene]
        for gene in dna2:
            self.dna[gene] += dna2[gene]

    def mutate(self):
        """random chance of gene mutation"""
        rand = random.randint(1, 100)
        if rand <= 50:
            self.dna[random.randrange(5)] += 1
        elif rand > 50:
            self.dna[random.randrange(5)] -= 1
