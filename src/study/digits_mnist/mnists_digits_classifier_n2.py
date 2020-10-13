from src import network2
import numpy as np

from src.study.utils import downloader
from src.study.mnist_common import mnist_reader


def download_mnist_digits_data():
    downloader.download_data("http://yann.lecun.com/exdb/mnist",
                                   ["train-images-idx3-ubyte.gz",
                                    "train-labels-idx1-ubyte.gz",
                                    "t10k-images-idx3-ubyte.gz",
                                    "t10k-labels-idx1-ubyte.gz"])

download_mnist_digits_data()

def train_model():

    net = network2.Network([784,30,10])

    training_data,test_data = mnist_reader.load()

    net.train("mnists_digits_classifier_n2.learnings",training_data, epochs=70, mini_batch_size=10, eta=0.001,
            test_data=test_data)

    return net

def print_result(actual,expected):
    print("%s is detected as %s" % (expected,actual))

def evaluate(net):
    training_data, test_data = mnist_reader.load()

    for test_sample in test_data[9000:]:
        print_result(np.argmax(net.feedforward(test_sample[0])), test_sample[1])

evaluate(train_model())