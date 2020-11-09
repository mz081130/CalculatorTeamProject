
from calculator.Addition import addition
from calculator.Division import division


def mean(numbers):
    n = len(numbers)
    t = 0
    for x in range(0, n, 1):
        t = addition(t, numbers[x])
    z = float(division(n, t))
    return z
