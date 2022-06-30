# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:58:58 2021

    Lecture03-1: Python NumPy Overview
        1. NumPy Arrays 
         1.1 Function for displaying properties of an array
        2. Element-wise processing of an array
         2.1 List construction from list comprehension
         2.2 Element-wise processing with np.sin
        3. Building a multi-dimensional array
        4. Slicing an array
        5. Selecting subsections
        6. Understanding How Array Memory Works
         6.1 Copying of an array
         6.2 Viewing, Pass-by-Reference vs. Copying
        7. Advanced indexing: Creating copies
        8. Slicing: Creating views
        9. Advanced Indexing (AI) with integer list : Copying
       10. Handling overlapping memory blocks: Reusing memory
        
"""
print()
print("===================================================")
print(" Lecture03-1: Python NumPy Overview  ")
print("===================================================")
print()


import numpy as np


#########################################################
#  1. NumPy Arrays 
#########################################################
print("##################################################")
print(" 1. NumPy Arrays")
print("##################################################")
print()

xarr = np.array([1,2,3], dtype=np.float32)

print()
print("****************************************")
print("    NumPy properties of Array ")
print("****************************************")
print("xarr:", xarr)
print("xarr.itemsize:", xarr.itemsize)
print("xarr.size:",  xarr.size)
print("xarr.ndim:",  xarr.ndim)
print("xarr.shape:", xarr.shape)
print("xarr.dtype:", xarr.dtype)
print("****************************************")
print()

#########################################################
#  1.1 Function for displaying properties of an array
#########################################################
print("##################################################")
print(" 1.1 Function for displaying properties of an array")
print("##################################################")
print()

def show_property(arr, name="arr"):    
    print("****************************************")
    print("    NumPy properties of", name, "array")
    print("****************************************")
    print(name + ":")
    print(arr)
    print(name + ".itemsize:", arr.itemsize)
    print(name + ".size:",  arr.size)   # No. of items
    print(name + ".ndim:",  arr.ndim)   # Np. of dimesion
    print(name + ".shape:", arr.shape)  # (row, col, ...)
    print(name + ".dtype:", arr.dtype)  # item type
    print("****************************************")
    print()

show_property(xarr, "xarr")

#########################################################
#  2. Element-wise processing of an array
#########################################################

print("##################################################")
print(" 2. Element-wise processing of an array")
print("##################################################")
print()

#########################################################
#  2.1 List construction from list comprehension
#########################################################
print("##################################################")
print(" 2.1 List construction from list comprehension")
print("##################################################")
print()

from math import sin

sinlist = [sin(i) for i in [1,2,3]] # Loop comprehension

print("sinlist from loop comprehension: ", sinlist) 
print()

sinlist = [round(sin(i), 3) for i in [1,2,3]] # Loop comprehension

print("sinlist from loop comprehension: ", sinlist)
print()

#########################################################
#  2.2. Element-wise processing with np.sin
#########################################################
print("##################################################")
print(" 2.2 Element-wise processing with np.sin")
print("##################################################")
print()

sinarr = np.sin(np.array([1,2,3], dtype=np.float32))
show_property(sinarr, "sinarr")

#########################################################
#  3. Building a multi-dimensional array
#########################################################
print("##################################################")
print(" 3. Building a multi-dimensional array")
print("##################################################")
print()
marr = np.array([ [1,2,3], [4,5,6] ])
show_property(marr, "marr")

#########################################################
#  4. Slicing an array
#########################################################
print("##################################################")
print(" 4. Slicing an array")
print("##################################################")
print()

col1 = marr[:, 0]  # 1st column
col2 = marr[:, 1]  # 2nd column
col3 = marr[:, 2]  # 3rd column

row1 = marr[0, :]  # 1st row
row2 = marr[1, :]  # 2nd row

show_property(col1, "col1")
show_property(col2, "col2")
show_property(col3, "col3")

show_property(row1, "row1")
show_property(row2, "row2")


#########################################################
#  5. Selecting subsections
#########################################################
print("##################################################")
print(" 5. Selecting subsections")
print("##################################################")
print()

sub1 = marr[:, 1:]     # all rows, the 2nd column thru the last column
sub2 = marr[:, ::2]	   # all rows, every other column
sub3 = marr[:, ::-1]   # reverse order of columns

show_property(sub1, "sub1")
show_property(sub2, "sub2")
show_property(sub3, "sub3")

print("sub1:")
print(sub1)
print("sub2:")
print(sub2)
print("sub3:")
print(sub3)
print()


#########################################################
#  6. Understanding How Array Memory Works
#########################################################
print("##################################################")
print("  6. Understanding How Array Memory Works")
print("##################################################")
print()

#########################################################
#  6.1 Copying of an array
#########################################################
print("##################################################")
print("  6.1 Copying of an array")
print("##################################################")
print()

# Create all ones 3x3 array
onesarr = np.ones((3, 3))
#show_property(onesarr, "onesarr")
print(onesarr)
print()

cparr = onesarr.copy()
cparr[0, 0] = -999
#show_property(cparr, "cparr")
print(cparr)
print()


dup1 = onesarr[:, [0, 1, 2, 2]]  # duplicate 3rd column
#show_property(dup1, "dup1")
print(onesarr[:, [0, 1, 2, 2]])
print()

dup2 = cparr[:, [0, 1, 2, 0]]    # duplicate 1st column
#show_property(dup2, "dup2")
print(cparr[:, [0, 1, 2, 0]])
print()

#########################################################
#  6.2 Viewing, Pass-by-Reference vs. Copying
#########################################################
print("##################################################")
print("  6.2 Viewing, Pass-by-Reference vs. Copying")
print("##################################################")
print()

dup1 = onesarr[:, [0, 1, 2, 2]]  # duplicate 3rd column
extarr = dup1                    # creates a view
extarr[0, 0] = -999

show_property(dup1, "dup1")
show_property(extarr, "extarr")

show_property(onesarr, "onesarr")

#########################################################
#  7. Advanced indexing: Creating copies
#########################################################
print("##################################################")
print("  7. Advanced indexing: Creating copies")
print("##################################################")
print()

# Create 2-D, 3x3 NumPy array
arr33 = np.ones((3,3))
show_property(arr33, "arr33")

# Duplicate the last dimension (column)
arr34 = arr33[:, [0,1,2,2]]
show_property(arr34, "arr34")

# Assign a new element to arr33 
arr33[0,0] = 999
print("After assigning an element to arr33\n")
show_property(arr33, "arr33")
show_property(arr34, "arr34")

#########################################################
#  8. Slicing: Creating views
#########################################################
print("##################################################")
print("  8. Slicing: creating views")
print("##################################################")
print()

# Create 2-d NumPy array
brr33 = np.ones((3,3))
show_property(brr33, "brr33")

# Slicing brr33
brr22 = brr33[:2, :2]  # No advanced indexing --> creates a view
show_property(brr22, "brr22")

# Assign a new element to brr33 
brr33[0,0] = 999
print("After assigning an element to brr33\n")
show_property(brr33, "brr33")
show_property(brr22, "brr22")


#########################################################
#  9. Advanced Indexing (AI) with integer list : Copying
#########################################################
print("##################################################")
print("  9. Advanced Indexing with integer list : Copying")
print("##################################################")
print()

# Create an array
carr5 = np.arange(5)  
show_property(carr5, "carr5")

# Index by integer list to force copy
carr3 = carr5[[0, 1, 2]]   # Advanced indexing : 
show_property(carr3, "carr3")
 
# Slicing 
carr4 = carr5[:4]    # Creates view
show_property(carr4, "carr4")

# Change element of carr5
carr5[0] = 999
print("After assigning an element to carr5\n")
show_property(carr5, "carr5")
show_property(carr3, "carr3")
show_property(carr4, "carr4")


#########################################################
#  10. Handling overlapping memory blocks:
#      Reusing memory
#########################################################
print("#######################################################")
print("  10. Handling overlapping memory blocks: Reuse memory ")
print("#######################################################")
print()

from numpy.lib.stride_tricks import as_strided

#########################################################
# as_strided(org, dim_tuple, overlap_step_tuple)
#   step_tupe, (4,4): (4, 4): Reuse memory by sliding 4 bytes along the columns and rows
#########################################################

n = 8
k = 5
x = np.arange(n)
y1 = as_strided(x, (k, n-k+1), (x.itemsize,)*2)
print("x:")
print(x)
print()
print("y1:")
print(y1)
print()

y2 = as_strided(x, (k, n-k+1), (4,4))
print("y2:")
print(y2)
print()

y3 = as_strided(x, (k+2, n-k+1), (4,4))
print("y3:")
print(y3)
print()

y4 = as_strided(x, (k+5, n-k+1), (4,4))
print("y4:")
print(y4)
print()

# Assign every other value
x[::2] = 99
print("x:")
print(x)
print()
print("y1:")
print(y1)
print()
print("y4:")
print(y4)
print()

