from src import network2
import mnist_fashion_classifier;

from src.study.mnist_common import mnist_reader

def train_model():

    net = network2.Network([784,30,10])

    training_data,test_data = mnist_reader.load()

    net.train("mnists_fashion_classifier_n2.learnings",
              training_data=training_data,
              epochs=100,
              mini_batch_size=10,
              eta=0.0001,
              test_data=test_data
              )

    return net

if __name__ == "__main__":
    mnist_fashion_classifier.evaluate(train_model())
