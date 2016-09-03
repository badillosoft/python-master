from random import rand
from math import *

class Node:
    def __init__(self, n):
        self.n = n
        self.w = []
        self.w0 = rand()

        for i in range(0, n):
            self.w.append(rand())

    def eval(self, x):
        s = self.w0
        for i in range(0, self.n):
            s += self.w[i] * self.x[i]

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
    def __init__(self, M, N, K):
        self.layers = []

        for i in range(0, M + 1):
            if i == 0:
                nodes = []

                for j in range(0, K):
                    nodes.append(0)

                self.layers.append(nodes)

                continue

            