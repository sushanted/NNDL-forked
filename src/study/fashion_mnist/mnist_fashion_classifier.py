
import matplotlib
matplotlib.use('TkAgg')

from src import network
import numpy as np

from src.study.utils import downloader
from src.study.utils import learning_recorder as recorder
from src.study.mnist_common import mnist_reader

items = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle","boot"]

def download_mnist_fashion_data():
    downloader.download_data("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com",
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

    training_data,test_data = mnist_reader.load()

    net.train("mnists_fashion_classifier.learnings", training_data, epochs=200, mini_batch_size=100, eta=0.05,
              test_data=test_data)

    #[784,30,10] : 40,10,0.1 : 57.36, 62.22
    #[784,30,10] : 40,10,0.01 : 58.59

    return net


def print_result(actual,expected):
    print("%s is detected as %s" % (items[expected],items[actual]))


def evaluate(net):

    training_data, test_data = mnist_reader.load()

    for test_sample in test_data[9000:]:
        print_result(np.argmax(net.feedforward(test_sample[0])),test_sample[1])

evaluate(train_model())












