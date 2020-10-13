# A network NOT learning anything, due to positional variance of the same input

from src import network
import numpy as np

input_size = 100
sample_size = 10000
fixed_numbers = np.random.random(input_size)


def evaluation_function(test_tuples,feedforwarder):
    current_cost = sum([ abs(feedforwarder(input)-expected) for (input,expected) in test_tuples ])
    print(current_cost)
    return current_cost[0][0]+current_cost[1][0]

def get_shuffled_fixed_numbers():
    sample = np.array(fixed_numbers)
    np.random.shuffle(sample)
    return sample

def generate_data():

    samples = [(get_shuffled_fixed_numbers().reshape((-1,1)),np.array([1,0]).reshape((-1,1))) for i in range(sample_size)]

    #print(samples)

    random_samples = [
                (
                    np.random.random(input_size).reshape((-1,1)),
                    np.array([0,1]).reshape((-1,1))
                 ) for i in range(sample_size)
            ]

    for sample in random_samples:
        samples.append(sample)

    np.random.shuffle(samples)

    return samples

# TODO : remove
def get_data_tuple(test,input,res):
    input.shape = (2, 1)
    if test:
        result = res

    else:
        result = np.array(res)
        result.shape = (1, 1)
    return (input,result)


def train_model():

    print("Generating model: ")

    training_data, test_data = (generate_data(),generate_data())

    #print(training_data)

    net = network.Network([input_size,30, 2],evaluation_function)

    print("Training model: ")

    net.train("function_learning.learnings",training_data, epochs=60, mini_batch_size=10,eta=5.0, test_data=test_data)

    return net




train_model()