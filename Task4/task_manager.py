from stack import Stack

class TaskManager:
    '''
        Класс TaskManager, данный класс отвечает за добавление и удаление задач с заданным приоритетом
            Данный класс включает в себя следующие методы:
                *   def __inint__ - метод контруктор класса, тут мы инициализируем элемент класса tasks, типа
                                    dict(словаря), в данном словаре будут хранится наши задачи с приоритетами

                *   def add_new_task - метод по добавлению новой задачи в стек с заданным приоритетом.
                                       В самом методе мы делаем проверку на наличие заданного приоритета, если
                                       он существует, то новая задача просто добавится к уже имеющемуся приоритету,
                                       если такого приоритета нет, то задача добавится с новым приоритетом в стек

                *   def delete_task - метод по удалению задачи из стека по названию задачи. В данном методе создаем
                                      временный стек для хранения задач и приоритетов, которые не нужно удалять

                *   def __str__ - метод по визуальному отображению информации для пользователя
    '''

    def __init__(self):
        '''Конструктор - класса'''

        self.tasks = dict()



    def add_new_task(self, text_task: str, priority: int):
        '''Метод по добавлению новой задачи в стек с заданным приоритетом'''

        # Если номера с таким приоритетом нет в стеке, то добавляем его
        if priority not in self.tasks:
            self.tasks[priority] = Stack()

        # Добавление задачи в стек с таким приоритетом
        self.tasks[priority].add_element(text_task)


    def delete_task(self, text: str):
        '''Метод по удалению задачи по тексту задачи из стека'''

        for stack in self.tasks.values():
            temp_stack = Stack()        # временный стек, который хранит задачи, которые не нужно удалять

            while not stack.check_stack_empty():
                task = stack.del_element()
                if task != text:
                    temp_stack.add_element(notes=task)

            while not temp_stack.check_stack_empty():       # Перемещаем оставшиеся задачи обратно в стек
                stack.add_element(temp_stack.del_element())


    def __str__(self):
        sorted_keys = sorted(self.tasks.keys())
        out_tasks = list()

        for key in sorted_keys:
            task_line = [str(key)]
            temp_stack = Stack()

            while not self.tasks[key].check_stack_empty():
                task = self.tasks[key].del_element()
                temp_stack.add_element(notes=task)

            while not temp_stack.check_stack_empty():
                task_line.append(temp_stack.del_element())

            out_tasks.append(', '.join(task_line))

        return '\n'.join(out_tasks)



