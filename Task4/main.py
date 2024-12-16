from task_manager import TaskManager


if __name__ == '__main__':
    manager = TaskManager()
    manager.add_new_task(text_task='поработать', priority=1)
    manager.add_new_task(text_task='Отдохнуть', priority=2)
    manager.add_new_task(text_task='поесть', priority=3)
    manager.add_new_task(text_task='убраться в квартире', priority=1)
    manager.add_new_task(text_task='Сходить на тренировку', priority=3)

    print(manager)
    print()
    manager.delete_task(text='Отдохнуть')
    print('Как выглядит стек после удаления одной задачи: ')
    print(manager)
