

class Rectangle:
    '''
        Класс Rectangle, данный класс отвечает за создание прямоугольника и дальнейшая с ним работа.
            Данный класс включает в себя следующие методы:
                *   def __init__ - метод конструктор класса, тут мы инициализируем элементы класса: width, height,
                                   элементу height мы указываем, что в случае чего по умолчанию ставить None. Затем
                                   мы сразу делаем проверку на то, что хранится у нас в height, если там None, то
                                   мы присваиваем height значение width, иначе просто приводим к типу int.

                *   def perimetr_rec - Метод по нахождению периметра прямоугольника. Если у нас высота равна ширине,
                                       то мы рассчитываем периметр квадрата. В противном случае рассчитываем периметр
                                       прямоугольника. Формула:
                                                    P (прямоугольника) = 2 * (a + b)
                                                    P (квадрата) = 4 * a

                *   def area_rec - Метод по нахождению площади прямоугольника. Если у нас высота равна ширине, то
                                   рассчитываем площадь квадрата. В противном случае рассчитываем площадь прямоугольника.
                                   Формула:
                                                    S (прямоугольника) = a * b
                                                    S (квадрата) = a * a

                *   def __add__ - Магический метод для операции сложения. В данном методе мы складываем периметры 2-х
                                  прямоугольников для получения нового и затем получаем новую ширину и высоту
                                  прямоугольника и возвращаем новый прямоугольник.

                *   def __lt__ - Магический метод для операции сравнения "меньше". В данном методе мы сравниваем площади
                                 2-х прямоугольников и если площадь 1-ого прямоугольника меньше площади 2-ого
                                 прямоугольника, мы возвращаем True иначе False.

                *   def __eq__ - Магический метод для операции сравнения "равно". В данном методе мы сравниваем площади
                                 2-х прямоугольников и если площадь 1-ого прямоугольника равна площади 2-ого
                                 прямоугольника, мы возвращаем True иначе False.

                *   def __le__ - Магический метод для операции сравнения "меньше или равно". В данном методе мы
                                 сравниваем площади 2-х прямоугольников и если площадь 1-ого прямоугольника меньше или
                                 равна площади 2-ого прямоугольника, мы возвращаем True иначе False.

                *   def __sub__ - Магический метод для операции для операции вычитания. В данном методе мы вычитываем
                                  периметры 2-х прямоугольников для получения нового и затем получаем новую ширину и
                                  высоту прямоугольника и возвращаем новый прямоугольник.

                *   def __str__ - Метод по визуальному отображению информации для пользователя

                *   def __repr__ - Метод по визуальному отображению информации для разработчика
    '''

    def __init__(self, width: int, height=None):
        '''Конструктор - класса'''
        self.width = width
        self.height = height

        if self.height == None:
            self.height = width
        else:
            self.height = int(height)


    def perimetr_rec(self):
        '''Метод по нахождению периметра прямоугольника'''
        result = 0
        if self.height == self.width:
            result = 4 * self.width
        else:
            result = 2 * (self.height + self.width)

        return result


    def area_rec(self):
        '''Метод по нахождению площади прямоугольника'''
        result = 0
        if self.height == self.width:
            result = pow(self.width, 2)
        else:
            result = self.height * self.width

        return result


    def __add__(self, other):
        '''Изменяем магический метод по операции сложения'''
        new_rect = self.perimetr_rec() + other.perimetr_rec()
        new_width = new_rect / 4
        new_height = new_width

        return Rectangle(width=new_width, height=new_height)


    def __lt__(self, other):
        '''Изменяем магический метод по операции "меньше" '''
        if self.area_rec() < other.area_rec():
            return True
        else:
            return False


    def __eq__(self, other):
        '''Изменяем магический метод по операции "равно" '''
        if self.area_rec() == other.area_rec():
            return True
        else:
            return False


    def __le__(self, other):
        '''Изменяем магический метод по операции "меньше либо равно" '''
        if self.area_rec() <= other.area_rec():
            return True
        else:
            return False



    def __sub__(self, other):
        '''Изменяем магический метод по операции вычитания'''
        new_rect = abs(self.perimetr_rec() - other.perimetr_rec())
        new_width = new_rect / 4
        new_height = new_width

        return Rectangle(width=new_width, height=new_height)



    def __str__(self):
        return f'Новая ширина: {self.width} и новая высота: {self.height} новый периметр = {self.perimetr_rec()}'


    def __repr__(self):
        return f'Rectangle{self.width, self.height}'






if __name__ == '__main__':
    rect1 = Rectangle(width=6, height=4)
    print(f'Периметр 1-ого прямоугольника с шириной: {rect1.width} и высотой: {rect1.height} = {rect1.perimetr_rec()}')
    print(f'Площадь 1-ого прямоугольника  с шириной: {rect1.width} и высотой: {rect1.height} = {rect1.area_rec()}')
    print()

    rect2 = Rectangle(width=7, height=7)
    print(f'Периметр 2-ого прямоугольника с шириной: {rect2.width} и высотой: {rect2.height} = {rect2.perimetr_rec()}')
    print(f'Площадь 2-ого прямоугольника  с шириной: {rect2.width} и высотой: {rect2.height} = {rect2.area_rec()}')
    print(rect1 + rect2)
    print(rect1 - rect2)
    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)
    print(rect1.__repr__())


