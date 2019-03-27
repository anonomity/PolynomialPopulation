from src.DNA import DNA
from matplotlib import pyplot as plt
import random

class population:


    def __init__(self, d, amount, cluster1, cluster2):
        self.d = d
        self.amount = amount
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.generations = 0
        numofClus = len(cluster1)



    def create_population(self,d,amount,cluster1,cluster2):
            self.cluster1 = cluster1
            self.cluster2 = cluster2
            self.d = d
            self.amount = amount
            matingpool = []
            popu = []
            self.popu = popu
            for i in range(amount):
                popu.insert(i,DNA(d,cluster1,cluster2))

            self.calc_fitness(amount,cluster1,cluster2)


            plt.show()
           # for y in range(amount):
           #     print(popu[y].score)



            self.matingpool = matingpool
            #calculate fitness


            finished = 0


            perfect_score = 10
            return popu


    def calc_fitness(self,amount,cluster1,cluster2):
        popu =self.popu
        for w in range(amount):
            popu[w].fitness(cluster1, cluster2)
            #print(popu[w].fitness(cluster1, cluster2))
            popu[w].plotDNA(cluster1, cluster2)
        return popu

    def natural_selection(self,pop,amount,cluster1,cluster2):

        self.pop = pop
        maxfitness = 0


        for i in range(amount):
            if (pop[i].fitness(cluster1,cluster2)) > maxfitness:
                    #print(pop[i].fitness(cluster1, cluster2))
                    maxfitness = pop[i].fitness(cluster1,cluster2)

        for w in range(amount):
            fit = pop[w].fitness(cluster1,cluster2)
            for i in range(fit):
                self.matingpool.insert(i,pop[w])
        return self.matingpool



    def newPop(self,pop,mp):

        self.mp = mp
        self.pop = pop
        length = len(pop)
        leng = len(mp)
        if leng > 0:
            for i in range(length):
                m = random.randint(0,leng-1)
                f = random.randint(0,leng-1)

                #random mother
                M = mp[m]
                #random father
                F = mp[f]

                child = M.crossover(F)

                self.pop[i] = child

        self.generations = self.generations + 1

        return self.pop


    def getAverageFitness(self,pop,cluster1,cluster2):
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.pop = pop

        popAvg = 0
        for i in range(len(pop)):
            popAvg = popAvg + pop[i].fitness(cluster1,cluster2)

        popPer = popAvg / (len(pop) * 10)
        return popPer