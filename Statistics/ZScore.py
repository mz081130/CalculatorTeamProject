from calculator.Division import division
from calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation


def zscore(numbers):
    u = mean(numbers)
    sig = standard_deviation(numbers)
    zsc = []
    for i in numbers:
        z = round(division(sig, subtraction(u, i)), 3)
        zsc.append(z)
    return zsc