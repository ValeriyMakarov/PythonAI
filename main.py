import numpy

from NetWork import NeuralNetwork
import matplotlib.pyplot

if __name__ == '__main__':
    train_set: list
    test_set: list
    with open("./datasets/mnist_train.csv", "r") as dataset_file:
        train_set = dataset_file.readlines()
    with open("./datasets/mnist_test.csv", "r") as dataset_file:
        test_set = dataset_file.readlines()

    net = NeuralNetwork(784,100,10,0.3)

    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))

        #matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        #matplotlib.pyplot.show()

        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        expected_output_array = numpy.zeros(10) + .01
        expected_output_array[int(all_values[0])] = .99
        net.train(scaled_array, expected_output_array)
        # print(train_set.index(item))

    index_query =0
    for item in train_set:
        all_values = item.split(',')
        #image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
        # matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        # matplotlib.pyplot.show()
        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        r = net.query(scaled_array)
        if numpy.argmax(r) == int(all_values[0]):
            index_query +=1
    print(f"Из {len(train_set)} правильно {index_query}: {index_query*100/len(train_set)}%")

    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))

        #matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        #matplotlib.pyplot.show()

        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        expected_output_array = numpy.zeros(10) + .01
        expected_output_array[int(all_values[0])] = .99
        net.train(scaled_array, expected_output_array)
        # print(train_set.index(item))

    index_query = 0
    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
        # matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        # matplotlib.pyplot.show()
        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        r = net.query(scaled_array)
        if numpy.argmax(r) == int(all_values[0]):
            index_query += 1
    print(f"Из {len(train_set)} правильно {index_query}: {index_query*100/len(train_set)}%")

    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))

        #matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        #matplotlib.pyplot.show()

        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        expected_output_array = numpy.zeros(10) + .01
        expected_output_array[int(all_values[0])] = .99
        net.train(scaled_array, expected_output_array)
        # print(train_set.index(item))

    index_query = 0
    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
        # matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        # matplotlib.pyplot.show()
        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        r = net.query(scaled_array)
        if numpy.argmax(r) == int(all_values[0]):
            index_query += 1
    print(f"Из {len(train_set)} правильно {index_query}: {index_query*100/len(train_set)}%")

    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))

        #matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        #matplotlib.pyplot.show()

        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        expected_output_array = numpy.zeros(10) + .01
        expected_output_array[int(all_values[0])] = .99
        net.train(scaled_array, expected_output_array)
        # print(train_set.index(item))

    index_query = 0
    for item in train_set:
        all_values = item.split(',')
        # image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
        # matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
        # matplotlib.pyplot.show()
        scaled_array = numpy.asfarray(all_values[1:]) / 255. * .99 + .01
        r = net.query(scaled_array)
        if numpy.argmax(r) == int(all_values[0]):
            index_query += 1
    print(f"Из {len(train_set)} правильно {index_query}: {index_query*100/len(train_set)}%")
    pass