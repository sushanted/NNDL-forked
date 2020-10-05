import network
import mnist_loader
import numpy as np

from PIL import Image, ImageFilter


def imageprepare(argv):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
        if (nheight == 0):  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
        newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    newImage.save(argv.replace('.png','_small.png'))

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    print(tva)
    return tva

def get_image_array(number):
    img_array=imageprepare('/Users/sravale/Personal/study/'+str(number)+'.png')#file path here
    img_array= np.array(img_array)
    img_array.shape=(784, 1)
    return img_array


def train_model():

    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    print(len(test_data[0][0]))
    print(test_data[0][0])

    #net = network.Network([784, 30, 10])

    #net.SGD(training_data, 12, 10, 3.0, test_data=test_data)

    #return net

def evaluate(net):
    for i in range(1,10):
        feedforward = net.feedforward(get_image_array(i))
        print(str(i)+" Is Guessed As: " + str(np.argmax(feedforward)))

    print(feedforward)


train_model()

#evaluate(train_model())

#img_array=imageprepare('/Users/sravale/Personal/study/tricolor2.png')#file path here

#for i in range(0,10):
    #imageprepare('/Users/sravale/Personal/study/'+str(i)+'.png')

#

#for i in range(0,10):

    #value = net.feedforward(test_data[i][0])

    #print(value)

    #print(str(np.argmax(value)) +" expected "+str(test_data[i][1]))



