import noise_detector;

from src import network2

def train_model():

    print("Generating model: ")

    training_data, test_data = (noise_detector.generate_data(False),noise_detector.generate_data(True))

    net = network2.Network([784, 30, 2])

    print("Training model: ")

    net.train("noise_detector_opt.learnings",
              training_data,
              epochs=20,
              mini_batch_size=5,
              eta=0.01,
              lmbda=0.0,
              test_data=test_data)

    return net

if __name__ == "__main__":
    noise_detector.evaluate(train_model())