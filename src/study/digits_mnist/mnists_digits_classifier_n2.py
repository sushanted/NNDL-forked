from src import network2

from src.study.mnist_common import mnist_reader

import mnists_digits_classifier

def train_model():

    net = network2.Network([784,100,10])

    training_data,test_data = mnist_reader.load()

    net.train("mnists_digits_classifier_n2.learnings",
              training_data=training_data,
              epochs=70,
              mini_batch_size=10,
              eta=0.001,
              lmbda=0.1,
              test_data=test_data
              )

    return net

if __name__ == "__main__":
    mnists_digits_classifier.evaluate(train_model())