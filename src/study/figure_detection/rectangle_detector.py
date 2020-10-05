

import network
import numpy as np

from PIL import Image, ImageFilter

max_width = 28
max_height = 28

def get_rect_image():
    img = np.zeros((max_width,max_height),int)

    left = np.random.randint(0, max_width-8)
    top = np.random.randint(0, max_height-8)

    right = np.random.randint(left+4,max_width-1)
    bottom = np.random.randint(top+4,max_height-1)

    value = 255
    img[top,left:right] = value
    img[bottom,left:right] = value
    img[top:bottom+1,left] = value
    img[top:bottom+1,right] = value

    return img

def get_noise_image():
    img = np.zeros((max_width,max_height),int)

    for i in range(0,80):
        img[np.random.randint(0,max_width),np.random.randint(0,max_height)] = 255

    return img


def generate_data(test):

    list = []
    for i in range(0, 10000):

        #Image.fromarray(np.uint8(image), 'L').save('data/image_r_' + str(i) + '.png')

        #Image.fromarray(np.uint8(image), 'L').save('data/image_n_' + str(i) + '.png')
        list.append(get_data_tuple(test,get_rect_image(),[0,1]))
        list.append(get_data_tuple(test,get_noise_image(),[1,0]))

    return list

def get_data_tuple(test,image,res):
    image.shape = (784, 1)
    if test:
        result = np.argmax(res)
        # 0 : noise
        # 1 : rectangle
    else:
        result = np.array(res)
        result.shape = (2, 1)
    return (image,result)


def train_model():

    print("Generating model: ")

    training_data, test_data = (generate_data(False),generate_data(True))

    net = network.Network([784, 30, 2])

    print("Training model: ")

    net.SGD(training_data, 20, 12, 2.5, test_data=test_data)

    return net

def evaluate(net):

    cross_check_data_set = generate_data(True)
    i = 0
    for cross_check_data in cross_check_data_set:
        i += 1
        feedforward = net.feedforward(cross_check_data[0])
        label = ['noise','rectangle'][np.argmax(feedforward)]
        image = cross_check_data[0]
        image.shape = (28,28)
        Image.fromarray(np.uint8(image), 'L').save('data/'+label+'/image' + str(i) + '.png')



evaluate(train_model())