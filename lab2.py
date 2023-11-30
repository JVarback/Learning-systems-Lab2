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
locations = 52

# Skapar en random individ med alla locations i en lista
def random_individual(locations): 
    indv = random.sample(range(1,locations+1), locations-1)
    return indv

# Calculates the distance between two places
def distance_calc(coord1, coord2):
    x1, y1 = coord1[1], coord1[2]
    x2, y2 = coord2[1], coord2[2]

    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def fitness():
    pass

def crossover():
    pass

def mutation():
    pass

def selection():
    pass



individual = random_individual(locations)

print(distance_calc(data_list[0], data_list[1]))
