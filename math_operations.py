import numpy as np

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """This function takes two numbers a and b and multiplies them and returna the result."""
    return a * b

def mean(numbers):
    return np.mean(numbers)

numbers = [1, 2, 3]
print(mean(numbers))

print(add(10, 5))
