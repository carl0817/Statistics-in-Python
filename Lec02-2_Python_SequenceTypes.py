# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:58:58 2022

    Lecture02-2 Python Sequence Types
        1. Immutable sequence type data structures   
          1.1 Tuple type objects
          1.2 Range type objects
          1.3 String type objects --> discussed in 3. Text sequence type
          
        2. Mutable sequence type data structures
          2.1 List type objects
          2.2 Soft and hard copy
          
        3. Text sequence type: str
        
        4. Dictionary type objects
"""

def show_data(data, name="data"):    
    print("**********************************************")
    print(name + ":")
    print(data)
    print("Type of {0}: {1}".format(name, type(data)))
    print()

def existIn(item, seqObjName, seqObj):
    print("**********************************************")
    if item in seqObj: 
        print("True: {0} is in {1}: ".format(item, seqObjName))
    else:
        print("False: {0} is not in {1}: ".format(item, seqObjName))
    print()
    
print()
print("===================================================")
print(" Lecture02-2: Python Sequence Types  ")
print("===================================================")
print()

##################################################
#   1. Immutable sequence type data structures  
##################################################
print("##################################################")
print(" 1. Immutable sequence type data structures")
print("##################################################")
print()

# 1.1 Tuple: heterogenous sequence types in parentheses, ()
tpl1 = tuple('abc')   # Tuple from separating a string 
show_data(tpl1, "tpl1")

tpl2 = tuple([1, 2, 3])
show_data(tpl2, "tpl2")

# 1.2 in membership operation with tuple
existIn('a', "tpl1", tpl1)
existIn('"a"', "tpl1", tpl1)
existIn("\"'a'\"", "tpl1", tpl1)
existIn("\"'a'\"", "tpl2", tpl2)

# 1.3 Range function: ordered sequences of integers, used for looping 
rng1 = range(5)
show_data(rng1, "rng1")
print("list(range(5)):", list(range(5))) 
print()

rng2 = range(1, 10, 2)   
show_data(rng2, "rng2")
print("list(range(1,10,2)):", list(range(1, 10, 2))) 
print()

# 1.4 Used for looping a specific number of times in for loops 
for i in rng1:
    print("---" + str(i))
print()

for j in rng2:
    print("---" + str(j))
print()
  
##################################################
#   2. Mutable sequence type data structures  
##################################################
print()
print("##################################################")
print(" 2. Mutable sequence type data structures")
print("##################################################")
print()

# 2.1 List: heterogenous ordered sequence types in square brakets, []

list0 = [0, 2, 4, 6, 8, 10] 
list1 = list(range(5))
list2 = list(range(0, -10, -1))
list3 = list(range(1, 10, 2))

show_data(list0, "list0")
show_data(list1, "list1)")
show_data(list2, "list2")
show_data(list3, "list3")

print(list(range(5)))
print(list(range(0, -10, -1)))
print(list(range(1, 10, 2)))
print()

list4 = [x for x in range(5)]
show_data(list4, "list4")
#print("list4:", list4)

list5 = [x**2 for x in range(1,4)]
show_data(list5, "list5")
#print("list5:", list5)

list6 = [3, 4, 3.14, 'moon', 'sun', 'earth']
show_data(list6, "list6]")
print("list6[3]:", list6[3])
print()
print("list6[4]:", list6[4])
print()

list7 = [3, 4, 3.14, ['moon', 'sun', 'earth']]
show_data(list7, "list7")
print("list7[3][1]:", list7[3][1])
print()

list8 = [x**2 for x in list7 if type(x) == int]
show_data(list8, "list8")

# 2.2 Soft and hard copy

list9 = list(range(1,6))
softlist = list9        # soft copy, pass-by-reference
hardlist = list(list9)   # hard copy, pass-by-value
newlist = [x**2 for x in list9]
list9[1] = 0

print("\nAfter list9[1] = 0")
show_data(list9, "list9")
show_data(softlist, "softlist")
show_data(hardlist, "hardlist")
show_data(newlist, "newlist")

#print("list9:", list9)
#print("softlist:", softlist)
#print("hardlist:", hardlist)
#print("newlist:", newlist)s

##################################################
#   3. Text sequence type: str
##################################################
print()
print("##################################################")
print(" 3. Text sequence type: str")
print("##################################################")
print()

greet = "hello world"
greet1 = greet.capitalize()
print(greet.capitalize())
print(greet1)

print(greet.title())

print(greet.center(30))

print(greet.center(20))

words = ['moon', 'sun', 'earth']
orgstr = "".join(words)
print(orgstr)

orgrep = orgstr*3
print(orgrep)
print(orgrep.count(orgstr))

print("find: ", orgrep.find('sun'))
print("rfind: ", orgrep.rfind('sun'))

print(orgrep.replace('sun', 'jupiter'))

greetctr = greet.center(20)     # Center-alignment

greetleft = greet.ljust(20)
print(greet.ljust(20))

greetright = greet.rjust(20)
print(greet.rjust(20))

print(greetctr)
print(greetleft)
print(greetright)

print(len(greetctr))
greetrstp = greetctr.rstrip()
print(len(greetrstp))

greetlstp = greetrstp.lstrip()
print(greetlstp)
print(len(greetlstp))

upgreet = greet.upper()
print(upgreet)

lowgreet = upgreet.lower()
print(lowgreet)

greetlist = greet.split()
print(greetlist)

##################################################
#   4. Dictionary type objects
##################################################
print()
print("##################################################")
print(" 4. Dictionary type objects")
print("##################################################")
print()

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print('The third month is ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print('Apr and Jan are', dist, 'apart')
print()

monthNumbers['Jun'] = 6
monthNumbers['May'] = 'V'
print("monthNumbers:", monthNumbers)
print()

print("monthNumbers.keys() -->", monthNumbers.keys())
print()

print("monthNumbers.values() -->", monthNumbers.values())
print()

for key in monthNumbers:
    print("({0}, {1})".format(key, monthNumbers[key]))
print()   
    
print("keys to tuple: tuple(monthNumbers.keys()) -->\n", tuple(monthNumbers.keys()))
print()