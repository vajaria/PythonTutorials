# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:12:10 2017

@author: hvajaria
"""

a=[1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,5,5,6,7,8,8,9]

def printarray(a,length):
    for i in range(0,length):
        print(i,a[i])
    
printarray(a,len(a))
write_index=1;
# write_index is the location where we will write a new unique entry to
# we will start at 1 because the 0th entry will always be unique
for i in range(1,len(a)):
    # if this is same as the previous entry, keep going on
    if(a[i]==a[write_index-1]):    
        i=i+1
    # if this is a new entry, write it and advance position of write_index
    else:
        a[write_index]=a[i]
        write_index=write_index+1

        
printarray(a,write_index)        