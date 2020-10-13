
from src import network
import numpy as np

from src.study.utils import downloader
from src.study.mnist_common import mnist_reader

items = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle","boot"]

def download_mnist_fashion_data():
    downloader.download_data("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com",
                                   ["train-images-idx3-ubyte.gz",
                                    "train-labels-idx1-ubyte.gz",
                                    "t10k-images-idx3-ubyte.gz",
                                    "t10k-labels-idx1-ubyte.gz"])

download_mnist_fashion_data()

def train_model():

    net = network.Network([784,30,10])

    training_data,test_data = mnist_reader.load()

    net.train("mnists_fashion_classifier.learnings", training_data, epochs=70, mini_batch_size=4, eta=0.01,
              test_data=test_data)

    return net


def print_result(actual,expected):
    print("%s is detected as %s" % (items[expected],items[actual]))


def evaluate(net):

    training_data, test_data = mnist_reader.load()

    for test_sample in test_data[9000:]:
        print_result(np.argmax(net.feedforward(test_sample[0])),test_sample[1])

if(__name__ == "__main__"):
    evaluate(train_model())