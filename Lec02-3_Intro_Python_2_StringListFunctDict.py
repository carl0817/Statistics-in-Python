"""
Created on Wed Dec 29 14:58:58 2021

    Lecture02-3: More About Python String, List, Function, and Dictionary 
          
        1. String manipulation
        2. List manipulation
        3. Function definitions
        4. Function parameters: High-order functions
        5. Dictionary objects
"""

print("===================================================")
print(" Lecture02-3: More About Python String, List, Function, and Dictionary  ")
print("===================================================")
print()

#########################################################
#  1. String manipulation
#########################################################
print("===================================================")
print(" 1. String manipulation  ")
print("===================================================")

phrase = 'Tell the truth without blame and judgement.'
print("phrase:", phrase)
print(len(phrase))
print(phrase[5:])

phrase2 = phrase + " " + phrase
print(len(phrase2))
print(phrase2)

phrase3 = (phrase + " ") * 3 
print(phrase3)

print(phrase[5:8])

for ch in phrase:
    print(ch)

for i in range(len(phrase)):
    print(phrase[i], end="")

print()

words = phrase.split(sep=" ")
print(words)
print()

for word in words:
    print(word, end="-")
print()
    
#########################################################
#  2. List manipulation
#########################################################
print("===================================================")
print(" 2. List manipulation  ")
print("===================================================")

fruits = ['apple', 'watermelon', 'cherry']

for fruit in fruits:
    print(fruit)
print()

for i in range(len(fruits)):
    print(fruits[i])
print()

list1 = [x**2 for x in range(1,4)]
print(list1)
print()

org = [3, 4, 3.14, ['moon', 'sun', 'earth']]
list2 = [x**2 for x in org if type(x) == int]
print(list2)
print()

#########################################################
#  3. Function definition
#########################################################
print("===================================================")
print(" 3. Function definition  ")
print("===================================================")

# base = 3, exp = 3 ==> power(3, 3) returns 27

# Assume exp >= 0 
def power(base, exp):   
    if exp >= 0 :
        product = 1
        for i in range(exp): 
            product = product * base
    else: 
        product = None

    return product

def power2(base, exp):   
    return base**exp

print("power(2, -2)", power(2, -2))
print("power(2, 2)", power(2, 2))
print("power(2, 3)", power(2, 3))
print("power(2, 4)", power(2, 4))
print("power(2, 5)", power(2, 5))
print("power(2, 6)", power(2, 6))
print("power(2, 40)", power(2, 40))
print()
print("power2(2, -2)", power2(2, -2)) 
     
#########################################################
#  4. Function parameters: High-order functions
#########################################################
print("===================================================")
print(" 4. Function parameters for map() function")
print("===================================================")       

# e.g., fact(5) = 5! = 5*4*3*2*1
def fact(num):   
    if num > 0:
        product = 1
        for i in range(num, 0, -1): 
            product = product * i
    else: 
        product = None
    return product

print(fact(2))  # 2! = 2*1
print(fact(3))  # 3! = 3*2*1
print(fact(4))  # 4! = 4*3*2*1
print(fact(5))  # 5! = 5*4*3*2*1
print()

# e.g., powerOfTwo(3) = 2^3
def powerOfTwo(exp):
    if exp >= 0 :
        product = 1
        for i in range(exp): 
            product = product * 2
    else: 
        product = None
    return product


def applyToEach(list, func):
    """ Assumes list is a list and
        func(), a function parameter.
        Mutates list by applying func() 
        to each element, 
    """ 

    for i in range(len(list)):
        list[i] = func(list[i])
    print(list)

list = [-1, -2, -3, 4]
applyToEach(list, abs)
applyToEach(list, powerOfTwo)
applyToEach(list, fact)
print()

for i in map(fact, [1, 3, 5, 10]):
    print(i)
print()

l2 = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [4, 3, 2, 1]):
    l2.append(i)
print(l2)
print()

l3 = [i for i in map(lambda x, y: x**y, [1, 2, 3, 4], [4, 3, 2, 1])]
print(l3)
print()

#########################################################
#  5. Dictionary objects
#########################################################
print("===================================================")
print(" 5. Dictionary objects")
print("===================================================")      

birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine', 'Apr':'Diamond', 'May':'Emerald'}
months = birthStones.keys()
stones = birthStones.values()

print("birthStones:", birthStones)
print("keys():", months)
print("values():", stones)
print()

print('Before adding Pearl:', months)
print('values()', stones )
birthStones['Jun'] = 'Pearl'
print('After adding Pearl:', months)
birthStones['Jan'] = 'Opal'
print('After modifying Jan, birthStone list:', birthStones)
print('values()', stones)





