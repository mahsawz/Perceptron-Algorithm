# -*- coding: utf-8 -*-
"""GradientDescentForPerceptron-NOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J10JV3kQtMIWnG5qA_UWVtGOEspaslPz
"""

from random import randint

nor = [(0, 0), (0, 1), (1, 0), (1, 1)]
target = [1, 0, 0, 0]
w1 = randint(0, 100)
w2 = randint(0, 100)
b = randint(0, 100)
eta = 0.1

for i in range(10000):
    for j in range(len(nor)):
        x1 = nor[j][0]
        x2 = nor[j][1]
        y = w1 * x1 + w2 * x2 + b
        error = target[j] - y
        b = b + eta * error
        w1 = w1 + eta * x1 * error
        w2 = w2 + eta * x2 * error

print('w1 : ', w1)
print('w2 : ', w2)
print('b : ', b)