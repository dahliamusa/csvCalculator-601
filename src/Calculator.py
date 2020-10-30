from CsvReader import CsvReader


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return round(c, 9)


def square_val(a):
    a = int(a)
    c = a ** 2
    return c


def squareRoot_val(a, b):
    a = int(a)
    c = a ** (1 / 2)
    decimals = int(b[::-1].find('.'))
    if decimals == -1:
        return c
    return round(c, decimals)


class Calculator:
    result = 0

    def __init__(self):
        pass

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
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square_val(a)
        return self.result

    def squareRoot(self, a, b):
        self.result = squareRoot_val(a, b)
        return self.result
