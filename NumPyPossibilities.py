import numpy

print(numpy.array([1,2,3]))#создание массива
print(numpy.array([1,"2",True]))#создание массива из строк

a = numpy.array([1,2,3,3])
print(a[0])
print(a[ [0,0,0,1,0] ])#выводит список из элементов с указанными индексами
print(a[ [True, False, True, True] ])#выводит список из элементов если на указанном месте стоит true

b = a.reshape(2,2)#изменяет размерность

print(b)

print(b[1,0])
print(b[1][0])