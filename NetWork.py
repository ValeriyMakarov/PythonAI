import numpy.random
import scipy.special

class NeuralNetwork:

    def __init__(self, input_layer_size:int, hidden_layer_size:int, output_layer_size:int, learning_rate):
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.output_layer_size = output_layer_size
        self.learning_rate = learning_rate
        self.weight_input_hidden = numpy.random.random((hidden_layer_size, input_layer_size))-.5
        self.weight_hidden_output = numpy.random.random((input_layer_size, hidden_layer_size))-.5
        self._activation_function = lambda x: scipy.special.expit(x)

    def train(self):
        pass

    def query(self, inputs):
        inputs = numpy.array(inputs, ndmin=2).T
        hidden_layer = numpy.dot(self.weight_input_hidden, inputs)
        hidden_layer = self._activation_function(hidden_layer)
        output_layer = numpy.dot(self.weight_hidden_output, hidden_layer)
        output_layer = self._activation_function(output_layer)
        return output_layer