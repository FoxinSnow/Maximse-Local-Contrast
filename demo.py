import numpy as np
import matplotlib.pyplot as plt
import random
import maxContrast
 
def demo():
    x = []
    for i in range(0, 25):
        x.append(complex(np.sin(random.uniform(0, 3.14)), np.cos(random.uniform(0, 3.14))))
    for i in range(0, 10000):
        x.append(complex(0, 0))
  
    x = np.fft.ifft(x).real
    x = x[1500:3000]

    x1 = 100*(x - np.min(x))/(np.max(x) - np.min(x))
    plt.plot(x1, color = "red")
    #plt.show()
    
    x2 = maxContrast.max_contrast(x1, 0, 100)
    plt.plot(x2, "blue")
     
    plt.show()
        
demo()