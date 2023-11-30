import random

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