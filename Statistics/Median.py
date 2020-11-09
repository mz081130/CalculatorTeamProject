from calculator.Addition import addition
from calculator.Division import division


def median(numbers):
    n = len(numbers)
    numbers.sort()
    if n % 2 == 0:
        first_median = numbers[int(division(2, n))]
        second_median = numbers[len(numbers) // 2 - 1]
        med = division(2, addition(first_median, second_median))
    else:
        med = numbers[division(2, n)]
    return med