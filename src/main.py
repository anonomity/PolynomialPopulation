import random
from matplotlib import pyplot as plt
from src.population import population
import pdb
#how many dots do you want in each cluster
numOfClus= 50

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
d = 2  #degree
num = 1000 #maxpop
mutationRate = 0.2


#negative cluster
n = create_cluster(-5,-1,-7,-1)




#positive cluster
p = create_cluster(1,6,4,9)




first = population(d,num,n,p,mutationRate)
print("generation : " + str(first.generations))
p=first.create_population(d,num,n,p)

mf = first.natural_selection(p,num,n,p)

print("generation : " + str(first.generations) + " Average fitness = " + str(first.getAverageFitness(p,n,p)))

first.newPop(p,mf,mutationRate)

print("generation : " + str(first.generations))

first.calc_fitness(num,n,p)

print("generation : " + str(first.generations) + " Average fitness = " + str(first.getAverageFitness(p,n,p)))

for i in range(25):
    first.newPop(p,mf,mutationRate)
    first.calc_fitness(num,n,p)
    print("generation : " + str(first.generations) + " best bitch = " + str(first.getBest()))