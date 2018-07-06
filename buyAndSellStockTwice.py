# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:32:24 2017

@author: hvajaria
"""




def maxProfitInRange(i,j):
    global a
    minVal=10000    
    maxDiff=0
    for i in range(i,j):
        if(a[i]<minVal):
            minVal=a[i]    
        SellTodayProfit=a[i]-minVal
        if(SellTodayProfit>maxDiff):
            maxDiff=SellTodayProfit
            #print("Max Profit from day {0} to day {1} is maxDiff {2}".format(i,j, maxDiff))
    return maxDiff       
            
#a = [310,315,275,295,260,270,290,230,255,250]
a=[12, 11, 13, 9, 12, 8, 14, 13, 15]

maxDiff=0
minVal=10000
maxProfit=0

for s in range(0,len(a)):
    maxProfitF = maxProfitInRange(0,s+1)
    maxProfitS = maxProfitInRange(s+1,len(a))
    maxProfit  = max(maxProfit,maxProfitF+maxProfitS)
    print("Max Profit s {} F {} B {}. Total {}".format(s, maxProfitF,maxProfitS,maxProfit))
    
for i in range(2,5):
    print(i)
    