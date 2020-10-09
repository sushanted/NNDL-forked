
from src import network
import numpy as np
import string

word_length = 12
word_file_name = "data/word_var_len.txt"
number_of_words = 10000

def evaluation_function(test_tuples,feedforwarder):

    current_cost = sum([ abs(feedforwarder(input)-expected) for (input,expected) in test_tuples ])
    return current_cost[0][0]

def train_model():
    net = network.Network([12,100,100,100,1],evaluation_function)

    test_tuples = []
    with open(word_file_name) as word_file:
        test_tuples=([(get_vector(word),np.array([[1]])) for word in word_file.readlines()[:number_of_words]])

    sensible_words = len(test_tuples)
    [test_tuples.append((get_vector(get_random_word()), np.array([[0]]))) for i in range(sensible_words)]

    np.random.shuffle(test_tuples)


    net.train("sensible_word_detector_var_len.learnings",
              test_tuples[:number_of_words],
              epochs=100,
              mini_batch_size=5,
              eta=1.0,
              test_data=test_tuples[number_of_words:]
              )

    return net


def get_random_word():
    return ''.join(np.random.choice(list(string.ascii_lowercase),np.random.randint(5,word_length)))

def get_vector(word):
    # print(word)
    # a is 1/26, b is 2/26 and so on, z is 26/26=1
    array = np.array([(ord(ch)-96)/26.0 for ch in word.strip()])
    # add word end character with normalized value 0
    array = np.append(array, 0.0)
    # repeat all the numbers (in same sequence) in array till the array becomes a fixed length array
    array = np.pad(array, (0, word_length - len(array)), 'wrap')
    array.shape = (word_length, 1)
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

    with open(word_file_name) as word_file:
        evaluate_list(net, word_file.readlines(), lambda prob: prob < 0.55)

evaluate(train_model())










