from random import random
from math import *

class Node:
    def __init__(self, n):
        self.n = n
        self.w = []
        self.w0 = random()

        for i in range(0, n):
            self.w.append(random())

    def eval(self, x):
        s = self.w0
        for i in range(0, self.n):
            s += self.w[i] * x[i]

        return 1.0 / (1.0 + exp(-s))

class Layer:
    def __init__(self, Ni, No):
        self.nodes = []

        for i in range(0, No):
            self.nodes.append(Node(Ni))

        self.Ni = Ni
        self.No = No

    def eval(self, x):
        y = []

        for node in self.nodes:
            y.append(node.eval(x))

        return y

class RN:
    def __init__(self, M, N, K, G):
        self.layers = [Layer(K, N)]
        self.M = M

        for i in range(0, M):
            self.layers.append(Layer(N, N))

        self.layers.append(Layer(N, G))

    def eval(self, x):
        y = self.layers[0].eval(x)

        for i in range(1, self.M + 1):
            y = self.layers[1].eval(y)

        z = self.layers[self.M + 1].eval(y)

        return z

rn = RN(1, 4, 2, 1)

print rn.eval([0, 0])
print rn.eval([0, 1])
print rn.eval([1, 0])
print rn.eval([1, 1])