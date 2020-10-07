import sys
sys.path.append('../')
sys.path.append('../../')

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import network
import numpy as np

import utils.downloader
import mnist_reader

items = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle","boot"]

def download_mnist_fashion_data():
    utils.downloader.download_data("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com",
                                   ["train-images-idx3-ubyte.gz",
                                    "train-labels-idx1-ubyte.gz",
                                    "t10k-images-idx3-ubyte.gz",
                                    "t10k-labels-idx1-ubyte.gz"])

download_mnist_fashion_data()

def get_label_array(label):
    label_array = np.zeros(10)
    label_array[label] = 1.0
    return label_array.reshape((10,1))


def train_model():
    net = network.Network([784,30,10])

    training_images,training_labels = mnist_reader.load_mnist("data", "train")
    test_images, test_labels= mnist_reader.load_mnist("data", "t10k")

    training_data = [ (image.reshape(784,1),get_label_array(label)) for image,label in zip(training_images,training_labels) ]
    test_data = [ (image.reshape(784,1),label) for image,label in zip(test_images,test_labels) ]

    net.SGD(training_data, epochs=100, mini_batch_size=100, eta=0.1,
            test_data=test_data)

    return net


def print_result(actual,expected):
    print("%s is detected as %s" % (items[expected],items[actual]))


def evaluate(net):
    test_images, test_labels = mnist_reader.load_mnist("data", "t10k")
    test_data = [(image.reshape(784, 1), label) for image, label in zip(test_images[9000:], test_labels[9000:])]

    for test_sample in test_data:
        print_result(np.argmax(net.feedforward(test_sample[0])),test_sample[1])

evaluate(train_model())












