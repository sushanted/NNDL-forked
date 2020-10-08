import numpy as np
import string
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

min,max,final = None,None,None
for i in [3,1,4,1,6,7,9,2]:
    min = i if not min or min > i else min
    max = i if not max or max < i else max
    final = i
print(min,max,final)


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



