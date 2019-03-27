from DNA import DNA
import random
from matplotlib import pyplot as plt
import numpy as np
from population import population

#how many dots do you want in each cluster
numOfClus= 10

#Create the environment for the Polynomial
def create_cluster(x_min, x_max,y_min , y_max):

    x_list = list()
    y_list = list()

    for x in range(0,numOfClus):
        x_list.append(int(random.uniform(x_min, x_max)))
    for y in range(0,numOfClus):
        y_list.append(int(random.uniform(y_min, y_max)))

    p =plt.scatter(x_list, y_list, s=10)


    return x_list,y_list,p





#####################################################################################################

####parameters#####
d = 3  #degree
num = 49 #maxpop

#negative cluster
n = create_cluster(-5,-1,-7,-1)




#positive cluster
p = create_cluster(1,6,4,9)




first = population(d,num,n,p)
print("generation : " + str(first.generations))
p=first.create_population(d,num,n,p)

mf = first.natural_selection(p,num,n,p)


first.newPop(p,mf)

print("generation : " + str(first.generations))

first.calc_fitness(num,n,p)


def findBest(self, pop):


