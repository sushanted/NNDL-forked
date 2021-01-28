
import sensible_word_detector_var_len

from src import network2

def train_model():
    net = network2.Network([12,30,1],evaluation_function=sensible_word_detector_var_len.evaluation_function)

    test_tuples = sensible_word_detector_var_len.get_test_tuples()

    net.train("sensible_word_detector_var_len_opt.learnings",
              test_tuples[:sensible_word_detector_var_len.number_of_words],
              epochs=100,
              mini_batch_size=5,
              eta=0.1,
              lmbda=0.2,
              test_data=test_tuples[sensible_word_detector_var_len.number_of_words:]
              )

    return net

if __name__ == "__main__":
    sensible_word_detector_var_len.evaluate(train_model())










