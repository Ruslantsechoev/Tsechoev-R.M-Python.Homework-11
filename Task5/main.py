import math
import random

from shape_init import Shape



class Circle(Shape):
    '''Класс Circle(Круг) наследуется от родительского класса Shape

        Содержит методы:
            *   def __init__ - конструктор класса, принимает радиус круга, если r не указан, то по умолчанию будет
                                r = random.randint(1, 5, 0.1)

            *   def area - метод по рассчету площади круга, данный метод мы переопределяем для нашей фигуры

            *   def __str__ - магический метод, который отвечает за красивое отображение информации для пользователя'''


    def __init__(self, radius = random.randint(1, 5)):
        '''Конструктор класса'''
        self.radius = radius


    def area_shape(self):
        '''Переопределяем метод площади, для нашего круга'''
        return math.pi * pow(self.radius, 2)


    def __str__(self):
        return 'Круг, r={:d}, S={:.2f}'.format(self.radius, self.area_shape())




class Rectangle(Shape):
    '''Класс Rectangle(Прямоугольник) наследуется от родительского класса Shape

        Содержит методы:
            *   def __init__ - конструктор класса, принимает ширину и длину прямоугольника, если width и height
                               не указаны, то по умолчанию будет width, height = random.randint(1, 5)

            *   def area - метод по рассчету площади прямоугольника, данный метод мы переопределяем для нашей фигуры

            *   def __str__ - магический метод, который отвечает за красивое отображение информации для пользователя'''

    def __init__(self, width=random.randint(1, 20), height=random.randint(1, 20)):
        '''Конструктор класса'''
        self.width = width
        self.height = height


    def area_shape(self):
        '''Переопределяем метод нахождения площади'''
        return self.width * self.height


    def __str__(self):
        return f'Прямоугольник, ширина={self.width}, высота={self.height}, S={self.area_shape()}'



class Triangle(Shape):
    '''Класс Triangle(Треугольник) наследуется от родительского класса Shape

        Содержит методы:
            *   def __init__ - конструктор класса, принимает основание и высоту треугольника, если base и height
                               не указаны, то по умолчанию будет base, height = random.randint(1, 5)

            *   def area - метод по рассчету площади треугольника, данный метод мы переопределяем для нашей фигуры

            *   def __str__ - магический метод, который отвечает за красивое отображение информации для пользователя'''

    def __init__(self, base=random.randint(1, 20), height=random.randint(1, 20)):
        '''Конструктор класса'''
        self.base = base
        self.height = height


    def area_shape(self):
        '''Переопределяем метод нахождения площади'''
        return 0.5 * self.base * self.height


    def __str__(self):
        return f'Треугольник, основание={self.base}, высота={self.height}, S={self.area_shape()}'



if __name__ == '__main__':
    circle = Circle(radius=2)
    print(circle)
    print()

    rectangle = Rectangle(width=9, height=7)
    print(rectangle)
    print()

    triangle = Triangle(base=10, height=12)
    print(triangle)
    print()

    try:
        shape = Shape()
    except TypeError as e:
        print(f'TypeError, нельзя создать объект абстрактного класса: {e}')


