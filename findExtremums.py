import numpy as np
import matplotlib.pyplot as plt
import random

def find_extremums(array):
    peaks = []
    valleys = []
    extremums = []
    flag = 1
    if(array[1] >= array[0]):
        #find peak first
        flag = 1 
    else:
        #find valley first
        flag = 0
    
    #begin the loop
    for i in range(0, len(array)-1):
        if(flag == 1):
            if(array[i+1] >= array[i]):
                continue
            peaks.append(i)
            flag = 0
        elif(flag == 0):
            if(array[i+1] <= array[i]):
                continue
            valleys.append(i)
            flag = 1
    
    #merge and sort
    extremums = peaks + valleys
    extremums.sort()
    #print(extremums)
    
    return peaks, valleys, extremums