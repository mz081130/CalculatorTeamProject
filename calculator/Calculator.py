from calculator.Addition import addition
from calculator.Division import division
from calculator.Subtraction import subtraction
from calculator.Mulitplication import multiplication
from calculator.Square import square
from calculator.Squareroot import sqrt


# Calculator class
class Calculator:
    result = 0

    # class constructor
    def ___init___(self):
        pass

    # class functions

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(division(a, b), 9)
        return self.result

    def skuare(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = sqrt(a)
        return self.result
