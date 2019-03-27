from Polynomial import Polynomial
import numpy as np
import random
from matplotlib import pyplot as plt
import pdb




class DNA:


    def __init__(self, deg,cluster1,cluster2) -> object:
        genes = []
        a = []
        self.genes = genes
        self.a = a
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.deg = deg
        X = np.linspace(-5, 6, 10, endpoint=True)
        self.X = X
        if deg == 2:
            genes.append(Polynomial(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)))
            e = genes[0]
            a.append(e.coef[0])
            a.append(e.coef[1])
            a.append(e.coef[2])
        elif deg == 3:
            genes.append(Polynomial(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5),random.randint(-5, 5)))
            e = genes[0]
            a.append(e.coef[0])
            a.append(e.coef[1])
            a.append(e.coef[2])
        elif deg ==4:
            genes.append(Polynomial(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5),random.randint(-5, 5)))
            e = genes[0]
            a.append(e.coef[0])
            a.append(e.coef[1])
            a.append(e.coef[2])
        else:
            genes.append(Polynomial(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5),random.randint(-5, 5),random.randint(-5, 5)))
            e = genes[0]
            a.append(e.coef[0])
            a.append(e.coef[1])
            a.append(e.coef[2])




    def plotDNA(self,cluster1,cluster2):
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        y = self.genes[0]
        F = y(self.X)

        plt.plot(self.X, F)


    def retDeg(self):
        return self.deg


    def fitness(self,cluster1, cluster2):

        #print(cluster2)

        xclus = cluster1[0]
        yclus = cluster1[0]

        numOfClus = len(xclus)


        under = 0
        over = 0
        on = 0

        sunder = 0
        sover = 0

        polyy = []

        for i in range(numOfClus):
            polyy.append((self.a[0] + (self.a[1] * xclus[i]) + (self.a[2] * (xclus[i]**2))))

            if polyy[i] > int(yclus[i]):
                under += 1
            elif polyy[i] < int(yclus[i]):
                over += 1
            else:
                on += 1

        sxclus = cluster2[1]
        syclus = cluster2[1]

        spolyy = []

        for w in range(numOfClus):
            spolyy.append(self.a[0] + (self.a[1] * xclus[w]) + (self.a[2] * (xclus[w] ** 2)))
            if spolyy[w] > int(yclus[w]):
                sunder += 1
            elif spolyy[w] < int(yclus[w]):
                sover += 1
            else:
                on += 1

        fit1 = over - sunder
        fit1 = abs(fit1)
        fit2 = under - sover
        fit2 = abs(fit2)

        if (fit1 > fit2):
            fitnes = fit2
        else:
            fitnes = fit1

        if (fitnes == 0):
            score = 10
        elif (fitnes == 1):
            score = 7
        elif (fitnes == 2):
            score = 5
        elif (fitnes == 3):
            score = 3
        elif (fitnes == 4):
            score = 2
        elif (fitnes == 5):
            score = 1
        elif (fitnes > 5):
            score = 0

        self.score = score
        return score


    def crossover(self, DNAfather):

        child = DNA(self.retDeg(),self.cluster1, self.cluster2)

        midpoint = random.randint(0,len(child.genes))
        for i in range(len(child.genes)):
            if(i > midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = DNAfather.genes[i]

        return child
