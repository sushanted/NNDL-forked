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
    net = network.Network([6,100,100,100,1],evaluation_function)

    test_tuples = []
    with open("data/word_fix_len.txt") as word_file:
        test_tuples=([(get_vector(word),np.array([[1]])) for word in word_file.readlines()])

    sensible_words = len(test_tuples)
    [test_tuples.append((get_vector(get_random_word()),np.array([[0]]))) for i in range(sensible_words)]

    np.random.shuffle(test_tuples)

    print(len(test_tuples))

    #print(test_tuples)

    net.SGD(test_tuples[:10000], 100, 50, 0.9, test_data=test_tuples[10000:])

    return net


def get_random_word():
    return ''.join(np.random.choice(list("zxqjxkvbpgyfmwcuidrhsnioate"),np.random.randint(6,7)))

def get_vector(word):
    #print(word)
    # a is 1/26, b is 2/26 and so on, z is 26/26=1
    array = np.array([(ord(ch)-96)/26.0 for ch in word.strip()])
    #array = np.append(array,np.zeros(10-len(array)))
    array.shape = (6,1)
    return array


def evaluate_list(net,words,test):
    count = 0
    for word in words:
        prob = net.feedforward(get_vector(word))[0][0]
        if test(prob):
            count+=1
            print(word.strip() + " "+str(prob))
    print("miss %: "+str(count*100.0/len(words)))

def evaluate(net):

    evaluate_list(net,[get_random_word() for i in range(100)],lambda prob : prob >0.55)

    with open("data/word_fix_len.txt") as word_file:
        evaluate_list(net, word_file.readlines(), lambda prob: prob < 0.55)

evaluate(train_model())










