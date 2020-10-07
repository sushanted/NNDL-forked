import numpy as np
import string
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


print(np.put(np.zeros(10),3,1))

def meth():

    plt.axis([0, 10, 0, 1])

    for i in range(100):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(0.1)

    #plt.show()


    #print(ord('z')-96)/26.0

    arr = np.array([3,6,7,2,5])


    print(''.join(['5']))

    array = np.array([2,4,6,8])
    array = np.append(array,0)
    array = np.pad(array,(0,12-len(array)),'wrap')
    array.shape = (12,1)

    print(array)



