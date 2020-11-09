from calculator.Addition import addition
from calculator.Division import division
from calculator.Subtraction import subtraction
from calculator.Square import square
from calculator.Squareroot import sqrt
from Statistics.Mean import mean


def standard_deviation(numbers):
    n = len(numbers)
    c = 0
    t = 0
    for i in range(0, n, 1):
        c = subtraction(mean(numbers), numbers[i])
        t = addition(square(c), t)
    x = division((n - 1), t)
    return sqrt(x)