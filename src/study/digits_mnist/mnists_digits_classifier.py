
import matplotlib
matplotlib.use('TkAgg')

from src import network
import numpy as np

from src.study.utils import downloader
from src.study.utils import learning_recorder as recorder
from src.study.mnist_common import mnist_reader


def download_mnist_digits_data():
    downloader.download_data("http://yann.lecun.com/exdb/mnist",
                                   ["train-images-idx3-ubyte.gz",
                                    "train-labels-idx1-ubyte.gz",
                                    "t10k-images-idx3-ubyte.gz",
                                    "t10k-labels-idx1-ubyte.gz"])

download_mnist_digits_data()


def train_model():

    net = network.Network([784,30,10])

    training_data,test_data = mnist_reader.load()

    net.train("mnists_digits_classifier.learnings",training_data, epochs=100, mini_batch_size=100, eta=0.1,
            test_data=test_data)

    # [784,30,10] : 30,10,0.1 : 75.05
    # [784,30,10] : 100,100,0.1 : 86.81
    # [784,30,10] : 10,100,5.0 : 47.91

    return net


def print_result(actual,expected):
    print("%s is detected as %s" % (expected,actual))


def evaluate(net):
    training_data, test_data = mnist_reader.load()

    for test_sample in test_data[9000:]:
        print_result(np.argmax(net.feedforward(test_sample[0])), test_sample[1])

evaluate(train_model())