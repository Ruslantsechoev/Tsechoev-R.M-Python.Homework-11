

class Stack:
    '''
        Класс Stack, данный класс отвечает за хранение информации, в нашем случае за хранение задач с приоритетом
            Данный класс включает в себя следующие методы:
                *   def __init__ - метод контруктор класса, тут мы инициализируем элемент класса _stack,который
                                   является защищенным элементом класса, типа list(списка)

                *   def del_element - метод по удалению элемента из стека с помощью встроенного метода списка pop().
                                      По умолчанию pop() возвращает и удаляет последний элемент из списка.

                *   def add_element - метод по добавлению задачи в стек

                *   def check_stack_empty - метод по проверке стека на пустоту, сли стек пустой, то вернется значение 0

    '''

    def __init__(self):
        '''Конструктор класса'''

        self._stack =list()


    def del_element(self):
        '''Метод по удалению элемента из списка с помощью встроенного метода pop()'''

        if self.check_stack_empty():
            return None
        else:
            return self._stack.pop()



    def add_element(self, notes):
        '''Метод по добавлению задачи'''

        self._stack.append(notes)


    def get_top_stack(self):
        '''Получение верхнего элемента в стеке'''

        if self.check_stack_empty():
            return None
        else:
            return self._stack[-1]



    def check_stack_empty(self):
        '''Метод по проверке стека на пустоту'''

        return len(self._stack) == 0

