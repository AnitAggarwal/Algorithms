# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:39:32 2018

@author: Anit Aggarwal
"""

import numpy as np
import pandas as pd
import math
import random

M = int(input("Enter the size of population"))
N = int(input("Enter the length of each memeber"))

population = np.random.randint(2,size=(M,N))
print(population)

G = int(input("Enter the number of generations to be passed "))

def fitness_func(X):
    return (sum(X)*sum(X))


fitness_values= np.ndarray(shape=(M,1))
for g in range(G):
    for i in range(M):
        fitness_values[i]=fitness_func(population[i])
        
    combined_array = np.hstack((population,fitness_values))
    
    normalized_fitness_values = fitness_values/sum(fitness_values)
    
    previous_probability = 0.0 
    probability_of_selection= np.ndarray(shape=(M,1))
    
    for i in range(M):
        probability_of_selection[i,0] = previous_probability+ normalized_fitness_values[i]
        previous_probability = probability_of_selection[i,0]
    
    random_value1 = np.random.ranf()
    
    for i in range(M):
        if random_value1 < probability_of_selection[i]:
            idx1 = i
            break
        
    random_value2 = np.random.ranf()
    
    for i in range(M):
        if i == idx1:
            continue
        if random_value2<probability_of_selection[i]:
            idx2 = i
            break
    
    print(probability_of_selection[idx])
    print(idx1)
    
    print(probability_of_selection[idx])
    print(idx2)    
    
    parent1 = population[idx1, :]
    parent2 = population[idx2, :]
    
    print("Selected Parents for crossover")
    print(parent1)
    print(parent2)
    
    cpt1 = random.randint(1,len(parent1)-1)  
    
    offspring1= np.concatenate((parent1[0  : cpt1], parent2[cpt1 :  ]),axis=0)
    offspring2= np.concatenate((parent2[0  : cpt1], parent1[cpt1 :  ]),axis=0)
    
    print("Offsprings produced after crossover")
    print(offspring1)
    print(offspring2)
    
    probablityOfMutation=np.random.ranf()
    mutationPoint=random.randint(0,N-1) 
    R3=np.random.ranf()
    
    if R3>=probablityOfMutation:
        offspring1[mutationPoint]=(offspring1[mutationPoint] + 1)%2;
        print("Offspring 1 after undergoing mutation")
        print(offspring1)
        
    population[idx1, :] = offspring1
    population[idx2, :] = offspring2    
    
print("Population after",G,"Generations")   
print(population) 
        
