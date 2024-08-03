import matplotlib.pyplot as plt
import math


class Plot:
    def scatter(*arg):
        plt.scatter(arg)
    pass

class Multiplots:

    def __init__(self, shape):
        self.size = shape[0] * shape[1]
    
    def get_location(i: int, shape: tuple):
        # shape is a tuple in (m, n)
        rows, cols = shape
        assert i > rows * cols, "i must be smaller than size m x n"
        return math.ceil(i/shape[1]), i % shape[1]
