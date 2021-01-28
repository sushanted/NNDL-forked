from src import network2
import figure_detector;

def train_model():

    print("Generating model: ")

    training_data, test_data = (figure_detector.generate_data(False),figure_detector.generate_data(True))

    net = network2.Network([784, 30, 3])

    print("Training model: ")

    net.train("figure_detector_opt.learnings",
              training_data,
              epochs = 40,
              mini_batch_size=5,
              eta=0.001,
              lmbda=0.1,
              test_data=test_data)

    return net

if __name__ == "__main__":
    figure_detector.evaluate(train_model())