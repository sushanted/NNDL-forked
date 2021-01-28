# A network learning provided function

from src import network
import numpy as np

# z = 3x+4y
# (3*x**2+4*y**3+5)/12
# (x+y)/2

funct = lambda x,y : (3*x**3+2*y**2)/4

def evaluation_function(test_tuples,feedforwarder):

    current_cost = sum([ abs(feedforwarder(input)-expected) for (input,expected) in test_tuples ])
    return current_cost[0][0]


def generate_data(test):

    list = []
    for i in range(0, 20000):

        x = np.random.random()
        y = np.random.random()
        list.append(get_data_tuple(test,np.array([x,y]),funct(x,y)))


    return list

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

    training_data, test_data = (generate_data(False),generate_data(True))

    net = network.Network([2,30, 1],evaluation_function)

    print("Training model: ")

    net.train("function_learning.learnings",training_data, epochs=20, mini_batch_size=3,eta=15.0, test_data=test_data)

    return net

def evaluate(net):

    cross_check_data_set = generate_data(True)

    for cross_check_data in cross_check_data_set:
        feedforward = net.feedforward(cross_check_data[0])
        print(str(cross_check_data)+"\nExpected  : "+str(cross_check_data[1]*7)+"\nActual    : "+str(feedforward[0][0]*7))


if __name__ == "__main__":
    evaluate(train_model())