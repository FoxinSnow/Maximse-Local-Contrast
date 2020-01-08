import numpy as np
import matplotlib.pyplot as plt
import findExtremums

def max_contrast(signal, bottom, top):
    theRange = top - bottom
    result = signal
    peaks, valleys, extremums = findExtremums.find_extremums(signal)
    #peaks_y = np.zeros((1, len(peaks), 1))
    #valleys_y = np.zeros((1, len(valleys), 1))
    #extremums_y = np.zeros((1, len(extremums), 1))
    #plt.scatter(peaks, peaks_y)
    #plt.scatter(valleys, valleys_y)
    #plt.scatter(extremums, extremums_y)
    
    #add begin and end point to the list
    extremums = extremums + [0, len(signal)]
    extremums.sort()

    for k in range (0, len(extremums)-1):
        result[extremums[k]:extremums[k+1]] = np.floor(theRange * \
        (signal[extremums[k]:extremums[k+1]] - np.min(signal[extremums[k]:extremums[k+1]]))/ \
        (np.max(signal[extremums[k]:extremums[k+1]]) - np.min(signal[extremums[k]:extremums[k+1]])))
        
    return result