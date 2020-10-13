import numpy as np
import string
import time

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import os,shutil


arr = np.array([1,2,3])

arr = np.append(arr,[4,5,6])

print(arr.reshape((-1,1)))


def m2():
    labels = ['ellipse','rectangle','line']

    if os.path.exists('data/fixed_figures'):
        shutil.rmtree('data/fixed_figures')

    os.makedirs('data/fixed_figures')

    for label in labels:
        os.mkdir('data/fixed_figures/'+label)


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



