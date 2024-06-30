import matplotlib.pyplot as plt
import math

def get_size(size: int, row_number: int):
    # given an integer n, returns the size of the subplots needed
    return tuple(math.ceil(size/ row_number), row_number)

def get_location(i: int, shape: tuple):
    # shape is a tuple in (m, n)
    assert i > shape[0] * shape[1], "i must be smaller than size m x n"
    return math.ceil(i/shape[1]), i % shape[1]
