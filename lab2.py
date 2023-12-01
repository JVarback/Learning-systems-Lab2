import random
import re
import math
import numpy as np

# Data prep
with open('berlin52.tsp', 'r') as file:
    lines = file.readlines()

read_start = lines.index('NODE_COORD_SECTION\n') + 1

data_list = [re.findall(r'\d+\.\d+|\d+', line) for line in lines[read_start:] if line.strip()]
data_list = [data for data in data_list if len(data) >= 3]
data_list = [(int(data[0]), float(data[1]), float(data[2])) for data in data_list]



# Hyperparameters
pop_size = 20
locations = 52
k = 4

# Skapar en random individ med alla locations i en lista
def random_individual(locations): 
    
    indv = random.sample(range(1,locations+1), locations-1)
    indv.append(indv[0])
    return indv


# Calculates the distance between two places
def distance_calc(id1, id2):
    
    coord1 = data_list[id1-1]
    coord2 = data_list[id2-1]
    x1, y1 = coord1[1], coord1[2]
    x2, y2 = coord2[1], coord2[2]

    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

# Fitness == total distance travelled, so less is better
def fitness(individual):
    total_distance = 0
    #dist_list = []
    for i in range(len(individual)):
        if i+1 > 51:
            break
        distance = distance_calc(individual[i], individual[i+1])

        total_distance += distance
        #dist_list.append(distance)

    return total_distance    
    


def crossover(p1, p2):
    
    child1 = 0
    child2 = 0
    rand_idx = random.randint(1,len(p1)-1)

    child1 = p1[:rand_idx] + p2[rand_idx:]
    child2 = p2[:rand_idx] + p1[rand_idx:]
    
    return child1, child2

def mutation(c1, c2):
    idx1, idx2 = random.sample(range(1,len(c1)-1), 2)

    c1[idx1], c1[idx2] = c1[idx2], c1[idx1]
    
    idx1, idx2 = random.sample(range(1,len(c1)-1), 2)
    c2[idx1], c2[idx2] = c2[idx2], c2[idx1]

    return c1, c2
    


def tournament_selection(pop, k):
    nr1 = 999999
    nr2 = 999999

    for i in range(k):
        
        ind = random.choice(pop)

        if  ind < nr1:
            nr2 = nr1
            nr1 = ind
        elif ind < nr2:
            nr2 = ind
            
    return nr1,nr2

def start_end_connect(): # Behövs det en funktion för att connecta start och slutpunkt????
    pass



# Creates the entire population
def create_pop(population):
    pop_list = []

    for i in range(population):
        individual = random_individual(locations)

        pop_list.append(individual)
    
    return pop_list


first_pop = create_pop(pop_size)

pop_fitness = []
new_pop = []
population = []
best = 999999

for i in range(10000):
    
    population = new_pop
    new_pop = []
    if i == 0:
        population = first_pop

    for individ in population:
        indv_fit = fitness(individ)
        pop_fitness.append(indv_fit)


    for x in range(5):

        indv1, indv2 = tournament_selection(pop_fitness,k)

        for idx in range(len(population)):
            
            if indv1 == pop_fitness[idx]:
                parent1 = population[idx]
            if indv2 == pop_fitness[idx]:
                parent2 = population[idx]


        child1, child2 = crossover(parent1, parent2)

        child1, child2 = mutation(child1, child2)

        new_pop += [parent1] + [parent2] + [child1] + [child2]

    
    pop_fitness = []
    for individ in new_pop:
        indv_fit = fitness(individ)
        pop_fitness.append(indv_fit)
    
    sorted(pop_fitness)
    if pop_fitness[0] < best:
        best = pop_fitness[0]
        
        print('Generation:', i)
        print('Shortest distance:',pop_fitness[0])



""" Jag torr att vi har en fullt fungerande fitness funktion, som använder funktionen för beräkning av distansen.
Populations skapandet funkar bra, verkar vara helt random
Nästa steg är nog att börja med den faktiska genetiska algoritmen. 
Börja kolla på hur du kan välja individer, sortera lista efter minst värde??
Sedan bestäm en selection funktion, kanske turnament?? """