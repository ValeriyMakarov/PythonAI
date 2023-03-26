import numpy.random
import scipy.special

class NeuralNetwork:

    def __init__(self, input_layer_size:int, hidden_layer_size:int, output_layer_size:int, learning_rate):
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.output_layer_size = output_layer_size
        self.learning_rate = learning_rate
        self.weight_input_hidden = numpy.random.random((hidden_layer_size, input_layer_size))-.5
        self.weight_hidden_output = numpy.random.random((output_layer_size, hidden_layer_size))-.5
        self._activation_function = lambda x: scipy.special.expit(x)

    def train(self, inputs, expected):
        inputs = numpy.array(inputs, ndmin=2).T
        expected = numpy.array(expected, ndmin=2).T

        hidden_layer = numpy.dot(self.weight_input_hidden, inputs)
        hidden_layer = self._activation_function(hidden_layer)
        output_layer = numpy.dot(self.weight_hidden_output, hidden_layer)
        output_layer = self._activation_function(output_layer)

        output_errors = expected - output_layer
        hidden_errors = numpy.dot(self.weight_hidden_output.T, output_errors)#?
        self.weight_hidden_output += self.learning_rate * numpy.dot((output_errors * output_layer *
            (1.0 - output_layer)), numpy.transpose(hidden_layer))
        self.weight_input_hidden += self.learning_rate * numpy.dot((hidden_errors * hidden_layer *
            (1.0 - hidden_layer)), numpy.transpose(inputs))

    def query(self, inputs):
        inputs = numpy.array(inputs, ndmin=2).T
        hidden_layer = numpy.dot(self.weight_input_hidden, inputs)
        hidden_layer = self._activation_function(hidden_layer)
        output_layer = numpy.dot(self.weight_hidden_output, hidden_layer)
        output_layer = self._activation_function(output_layer)
        return output_layer