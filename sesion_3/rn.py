from random import random
from math import *

class Node:
    def __init__(self, n):
        self.n = n
        self.w = []
        self.w0 = (2 * random() - 1) * 0.001
        self.r = 0.1

        for i in range(0, n):
            self.w.append((2 * random() - 1) * 0.001)

    def eval(self, x):
        s = self.w0
        for i in range(0, self.n):
            s += self.w[i] * x[i]

        try:
            y = 2.0 / (1.0 + exp(-s)) - 1.0
        except:
            # print s,
            e = 0.0001
            if s < -e:
                y = -1.0
            elif s > e:
                y = 1.0
            else:
                y = 0.0

        self.y = y

        return y

    def fitness(self, delta):
        self.w0 -= delta * self.r
        for i in range(0, self.n):
            self.w[i] += self.r * delta

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

    def fitness(self, delta):
        for node in self.nodes:
            node.fitness(delta)

class RN:
    def __init__(self, M, N, K, G):
        self.layers = [Layer(K, N)]
        self.M = M
        self.N = N

        for i in range(0, M):
            self.layers.append(Layer(N, N))

        self.layers.append(Layer(N, G))

    def eval(self, x):
        y = self.layers[0].eval(x)

        for i in range(1, self.M + 1):
            y = self.layers[1].eval(y)

        z = self.layers[self.M + 1].eval(y)

        return z

    def fitness(self, x, zo):
        z = self.eval(x)
        
        s = 0

        for i in range(0, len(z)):
            s += zo[i] - z[i]

        delta = float(s) / len(z)

        for layer in self.layers:
            layer.fitness(delta)

if __name__ == "__main__":
    rn = RN(1, 16, 2, 1)

    for i in range(0, 5000):
        rn.fitness([1, 1], [0]) # 0 - SILLA
        rn.fitness([0.8, 0.6], [0]) # 0 - SILLA
        rn.fitness([2, 1.5], [0.5]) # 0.5 - MESA
        rn.fitness([2.3, 1.2], [0.5]) # 0.5 - MESA
        rn.fitness([4, 3], [1]) # 1 - CAMA
        rn.fitness([4.5, 4], [1]) # 1 - CAMA

    print rn.eval([1, 1])
    print rn.eval([2, 1.5])
    print rn.eval([4, 3])
    print rn.eval([5, 4])
    print rn.eval([0.5, 0.5])

