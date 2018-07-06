# -*- coding: utf-8 -*-
"""
Created on Sat May 19 06:51:10 2018

@author: hvajaria
"""

#Basic data types
#Tuple
a=(3,5)
print(type(a))
print("num elements == 3 in tuple ",a.count(3))
print("index of 3 ",a.index(3))
a = a + (3,7,9)
print("num elements in tuple ",a.count(3))
# find the next index of 3
print("index of 3 ",a.index(3,a.index(3)+1))
# check if a contains 7
print("Does a contain 7? ",a.__contains__(7))

#Range
print("Range")
r=range(5,10,1)
x=[]
y=[]
for i in r:
    x.append(i)
    y.append(i**2)
print(x,y)
print("Range Done\n")
#String
print("C:\\n 'a' \"x\" '\\' done")
print("C:\newfolder")
print(r"C:\newfolder")