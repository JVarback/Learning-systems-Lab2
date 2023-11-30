import random
import re

# Data prep
with open('berlin52.tsp', 'r') as file:
    lines = file.readlines()

read_start = lines.index('NODE_COORD_SECTION\n') + 1

data_list = [re.findall(r'\d+', line) for line in lines[read_start:] if line.strip()]
data_list = [data for data in data_list if len(data) >= 3]
data_list = [(int(data[0]), float(data[1]), float(data[2])) for data in data_list]


# Hyperparameters
locations = 52

# Skapar en random individ med alla locations i en lista
def random_individual(locations): 
    indv = random.sample(range(1,locations+1), locations-1)
    return indv

def fitness():
    pass

def crossover():
    pass

def mutation():
    pass

def selection():
    pass



individual = random_individual(locations)
print(individual)