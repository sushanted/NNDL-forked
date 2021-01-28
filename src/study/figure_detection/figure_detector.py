
from src import network
import numpy as np
import shutil,os

from PIL import Image, ImageDraw

max_width = 28
max_height = 28

labels = ['ellipse', 'rectangle', 'line']

def get_bounds():


    left = np.random.randint(0, 13)
    top = np.random.randint(0, 13)

    right = np.random.randint(max_width - 13, max_width - 1)
    bottom = np.random.randint(max_height - 13, max_height - 1)


    return (left,top,right,bottom)

def get_rect_image():
    img = np.zeros((max_width,max_height),int)

    left,top,right,bottom = get_bounds()

    value = 255
    img[top,left:right] = value
    img[bottom,left:right] = value
    img[top:bottom+1,left] = value
    img[top:bottom+1,right] = value

    return img

def get_line_image():

    img = np.zeros((max_width, max_height), int)

    left,top,right,bottom = get_bounds()

    image = Image.fromarray(np.uint8(img), 'L')
    draw = ImageDraw.Draw(image);
    draw.line((left, top, right, bottom), fill=255)

    #image.save('data/tmp'+str(i)+'.png')

    img = list(image.getdata())

    img = np.array(img)

    img.shape = (28,28)

    #for i in range(0,80):
        #img[np.random.randint(0,max_width),np.random.randint(0,max_height)] = 255

    return img

def get_ellipse_image():

    img = np.zeros((max_width, max_height), int)

    left,top,right,bottom = get_bounds()

    image = Image.fromarray(np.uint8(img), 'L')
    draw = ImageDraw.Draw(image);
    draw.ellipse((left, top, right, bottom), outline=255)

    #image.save('data/tmp'+str(i)+'.png')

    img = list(image.getdata())

    img = np.array(img)

    img.shape = (28,28)

    #for i in range(0,80):
        #img[np.random.randint(0,max_width),np.random.randint(0,max_height)] = 255

    return img


def generate_data(test):

    list = []
    for i in range(0, 10000):

        list.append(get_data_tuple(test,get_ellipse_image(), [1, 0, 0]))
        list.append(get_data_tuple(test,get_rect_image(),[0,1,0]))
        list.append(get_data_tuple(test,get_line_image(),[0,0,1]))

    return list

def get_data_tuple(test,image,res):
    image.shape = (784, 1)
    if test:
        result = np.argmax(res)
        # 0 : noise
        # 1 : rectangle
    else:
        result = np.array(res)
        result.shape = (3, 1)
    return (image,result)


def train_model():

    print("Generating model: ")

    training_data, test_data = (generate_data(False),generate_data(True))

    net = network.Network([784, 30, 3])

    print("Training model: ")

    net.train("figure_detector.learnings",
              training_data,
              epochs = 100,
              mini_batch_size=5,
              eta=0.07,
              test_data=test_data)

    return net

def create_dirs():

    if os.path.exists('data/fixed_figures'):
        shutil.rmtree('data/fixed_figures')

    os.makedirs('data/fixed_figures')

    for label in labels:
        os.mkdir('data/fixed_figures/' + label)

def evaluate(net):

    create_dirs()

    cross_check_data_set = generate_data(True)
    i=0
    for cross_check_data in cross_check_data_set:
        i+=1
        feedforward = net.feedforward(cross_check_data[0])
        argmax = np.argmax(feedforward)
        label = labels[argmax]
        # print(str(feedforward[argmax]))
        if(argmax!=cross_check_data[1]):
            image = cross_check_data[0]
            image.shape = (28,28)
            Image.fromarray(np.uint8(image), 'L').save('data/fixed_figures/'+label+'/image' + str(i)+"_"+str(int(feedforward[argmax]*100000))+'.png')


if __name__ == "__main__":
    evaluate(train_model())

