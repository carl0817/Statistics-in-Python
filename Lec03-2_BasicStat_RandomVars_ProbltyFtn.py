# -*- coding: utf-8 -*-
"""
Created on May 9 14:08:58 2022

    Lecture03-2: Basic Statistics 
        1. Two dice rolling

        
"""

#import numpy as np

print("******************************************************************")
print("  Lecture 3-2 : Basic Statistics - Random Variables ")
print("******************************************************************")
print()

##############################################################
#  1.  Two dice rolling
##############################################################

# Read June rents: the number of the rooms rented at a Bed & Breakfast
# Load rents.csv

sample_space = [(i,j) for i in range(1, 7) for j in range(1, 7)]
#sample_space = {(i,j) for i in range(1, 7) for j in range(1, 7)}

print()
print("************************************************************************")
print("    1. Two dice rolling") 
print("************************************************************************")
print("Sample space:")
print(sample_space)
print("{0} pairs are populated.".format(len(sample_space)))
print()

print("Random variable of die1 + die2:")
RV_add = {(i,j): i+j for i in range(1, 7) for j in range(1, 7) }
print(RV_add)
print()


from collections import defaultdict

print("Initial dinv:")
# Define a dictionary with values as list
# c.f., defaultdict(int)

dinv = defaultdict(list)
print(dinv)
print()

# Reverse key and data item
# items() method: returns a view object that 
# displays a list of dinctionary's (key, value) tuple pairs
for key, value in RV_add.items():
    dinv[value].append(key)

print("Sum of die1 and die2:")
print(dinv)
print()   

print("All possible sums:", len(dinv))
print(dinv.keys())
print()

print("List of the sum of die1 and die2 of 7:")    
print(dinv[7])
print("Only {0} pairs have a sum of 7.".format(len(dinv[7])))
print()

n_samples = len(sample_space)

sum = 0
pmf = defaultdict(float)

for key, value in dinv.items():
    prob = len(value) / n_samples
    pmf[key] = round(prob, 4)
    sum += prob
    
print("Probability of each sum:")
print(pmf)
print()

max_key = max(pmf, key=pmf.get)
print("max_key:", max_key)
print("dinv[max_key]:")
print(dinv[max_key])
print("Max Probability:", pmf[max_key])
print()

min_key = min(pmf, key=pmf.get)
print("min_key:", min_key)
print("dinv[min_key]:")
print(dinv[min_key])
print("Min Probability:", pmf[min_key])
print()

print("Sum of Probabilities of individual sums:", round(sum, 4))
print()

print("************************************************************************")
print()

