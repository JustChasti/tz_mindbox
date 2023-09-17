from abc import ABC, abstractmethod
import math


def check_params(function):
        def iternal(*args, **kwargs):
            parameters = (args + tuple(kwargs.values()))[1:]
            for i in parameters:
                if i <= 0:
                    raise Exception('arguments must be positive')
            if len(parameters) == 3:
                elements = sorted(parameters)
                if elements[0] + elements[1] <= elements[2]:
                    raise Exception('The sum of the 2 sides of a triangle must be greater than 3 side')
            return function(*args, **kwargs)
        return iternal


class Figure(ABC):
    square: float

    @abstractmethod
    def count_square(self):
        pass


class Triangle(Figure):    

    @check_params
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def count_square(self):
        p = (self.a + self.b + self.c)/2
        self.square = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return self.square

    def is_right(self):
        sides = sorted((self.a, self.b, self.c))
        if (math.pow(sides[0], 2) + math.pow(sides[1], 2)) == math.pow(sides[2], 2):
            return True
        return False


class Circle(Figure):

    @check_params
    def __init__(self, r) -> None:
        self.r = r

    def count_square(self):
        self.square = math.pi * math.pow(self.r, 2)
        return self.square
    

# как я понял в python нет compile-time, ведь это итерируемый язык, соответственно нет компиляции
# плэтому я предлагаю свой вариант вычисления площади без знания типа фигуры
def calculate_square(*args):
    if len(args) == 1:
        figure = Circle(args[0])
        return figure.count_square()
    elif len(args) == 3:
        figure = Triangle(args[0], args[1], args[2])
        return figure.count_square()
    else:
        raise Exception("there is no figure with these parameters")
    