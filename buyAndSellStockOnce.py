# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:32:24 2017

@author: hvajaria
"""

a = [310,315,275,295,260,270,290,230,255,250]

maxDiff=0
minVal=10000
maxVal=0
for i in range(0,len(a)):
    if(a[i]<minVal):
       minVal=a[i]    
    SellTodayProfit=a[i]-minVal
    if(SellTodayProfit>maxDiff):
        maxDiff=SellTodayProfit
        print("Max Profit till day i {0} is maxDiff {1}".format(i, maxDiff))