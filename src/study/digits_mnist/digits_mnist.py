import sys
sys.path.append('../')
sys.path.append('../../')

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import network
import numpy as np


import urllib2
import os.path
import utils.downloader

def download_mnist_digits_data():
    utils.downloader.download_data("http://yann.lecun.com/exdb/mnist",
                                   ["train-images-idx3-ubyte.gz",
                                    "train-labels-idx1-ubyte.gz",
                                    "t10k-images-idx3-ubyte.gz",
                                    "t10k-labels-idx1-ubyte.gz"])

download_mnist_digits_data()