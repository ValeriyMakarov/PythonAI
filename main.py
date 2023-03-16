from NetWork import NeuralNetwork

if __name__ == '__main__':
    net = NeuralNetwork(3,5,2,0.3)
    print (net.query([1,2,3]))