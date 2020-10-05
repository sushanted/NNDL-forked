import sys
sys.path.append('../../')

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import network
import numpy as np
import string

cost =[]

#for i in range(30):
#    print(''.join(np.random.choice(list(string.ascii_lowercase),(np.random.randint(5,11)))))

def evaluation_function(test_tuples,feedforwarder):

    current_cost = sum([ abs(feedforwarder(input)-expected) for (input,expected) in test_tuples ])
    cost.append(sum(current_cost)) # false positive + false negative
    return current_cost

def train_model():
    net = network.Network([10,30,30,30,1],evaluation_function)

    test_tuples = []
    with open("data/words.txt") as word_file:
        test_tuples=([(get_vector(word),np.array([[1]])) for word in word_file.readlines()])

    #sensible_words = len(test_tuples)
    #[test_tuples.append((get_vector(get_random_word()),np.array([[0],[1]]))) for i in range(sensible_words)]

    np.random.shuffle(test_tuples)

    #print(len(test_tuples))

    #print(test_tuples)

    net.SGD(test_tuples[:20000], 30, 100, 9.0, test_data=test_tuples[20000:])

    return net


def get_random_word():
    return ''.join(np.random.choice(list(string.ascii_lowercase),np.random.randint(5,11)))

def get_vector(word):
    # print(word)
    # a is 1/26, b is 2/26 and so on, z is 26/26=1
    array = np.array([(ord(ch)-96)/26.0 for ch in word.strip()])
    array = np.pad(array)
    array.shape = (10,1)
    return array


def evaluate(net):

    for word in ['hfjsds','dddwfj','vfddw','gqfdc','sdg']:
        print(word)
        print(net.feedforward(get_vector(word)))


    for word in ['apple','pineapple','flower','template','somebody']:
        print(word)
        print(net.feedforward(get_vector(word)))

evaluate(train_model())










