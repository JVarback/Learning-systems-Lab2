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

# Skapar en random individ med alla locations i en lista
def random_individual(locations): 
    indv = random.sample(range(1,locations+1), locations-1)
    
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
        if i+1 > 50:
            break
        distance = distance_calc(individual[i], individual[i+1])

        total_distance += distance
        #dist_list.append(distance)

    return total_distance    
    

    


def crossover():
    pass

def mutation():
    pass

def selection():
    pass

def start_end_connect(): # Behövs det en funktion för att connecta start och slutpunkt????
    pass


# Creates the entire population
def create_pop(population):
    pop_list = []

    for i in range(population):
        individual = random_individual(locations)

        pop_list.append(individual)
    
    return pop_list


population = create_pop(pop_size)

print(len(population))


""" Jag torr att vi har en fullt fungerande fitness funktion, som använder funktionen för beräkning av distansen.
Populations skapandet funkar bra, verkar vara helt random
Nästa steg är nog att börja med den faktiska genetiska algoritmen. 
Börja kolla på hur du kan välja individer, sortera lista efter minst värde??
Sedan bestäm en selection funktion, kanske turnament?? """