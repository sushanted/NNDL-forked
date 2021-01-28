# A network learning provided function

import function_learning

from src import network2

def train_model():

    print("Generating model: ")

    training_data, test_data = (function_learning.generate_data(False),function_learning.generate_data(True))

    net = network2.Network([2,30,1],evaluation_function=function_learning.evaluation_function)

    print("Training model: ")

    net.train("function_learning_opt.learnings",
              training_data=training_data,
              epochs=100,
              mini_batch_size=5,
              eta=0.05,
              test_data=test_data
              )

    return net

if __name__ == "__main__":
    function_learning.evaluate(train_model())