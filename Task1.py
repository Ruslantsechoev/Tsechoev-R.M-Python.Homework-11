import numpy as np

class Matrix:
    '''
        Класс Matrix, данный класс отвечает за создание и работу с матрицами
            Данный класс включает в себя следующие методы:
                *   def __init__ - метод конструктор класса, тут мы инициализируем элементы класса rows, columns
                                    matrix (rows - количество строк в матрице, columns - количество колонок в матрице
                                    matrix - единичная матрица размерностью rows*columns).

                *   def _check_input_value_for_matrix - метод по проверке веденных значений в матрицу в соответствии с
                                                        размерностью самой матрицы, если веденные значения соответствуют
                                                        размерности матрицы, то вернется True, иначе False

                *   def add_matrix - метод по сложению матриц. Для реализации сложения элементов матрицы, используем
                                    встроенный цикл, который проходит по всем элементам в матрице.

                *   def subtraction_matrix - метод по вычитанию матриц. Реализация идентична реализации сложения
                                             матриц.

                *   def multi_matrix - метод по умножению матриц. В начале мы делаем проверку матриц на соответствие
                                       размерности, т.е. кол-во строк 1-ой матрицы должны быть равны кол-ву колонок
                                       2-ой матрицы, если условие выполняется, то можем производить перемножение
                                       матриц. Для реализации алгоритма перемножения элементов матрицы используем
                                       встроенный цикл, который будет брать элемент из строки 1-ой матрицы и умножать
                                       на элемент столбца из 2-ой матрицы. Пример:

                                       1 2 3        10 20
                                       4 5 6        40 50
                                                    60 70

                                        умножение будет происходить так - 1*10 2*40 3*60
                                                                          4*20 5*50 6*70

                *   def transposition_matrix - метод по транспонированию матрицы. Для реализации транспонирования,
                                               используем встроенный цикл, который проходит по всем элементам старой
                                               матрицы и добавляет в новую матрицы элементы поменяв местами колонки со
                                               строками. Пример:

                                                старая матрица              новая матрица(транспонированная)
                                                    1 2 3                               1 4
                                                    4 5 6                               2 5
                                                                                        3 6
    '''

    def __init__(self, rows: int, columns: int):
        '''Конструктор-класса'''
        self.rows = rows
        self.columns = columns
        self.matrix = np.zeros((rows, columns), dtype="int")


    def _check_input_value_for_matrix(self, other):
        '''Метод по проверке веденных значений в матрицы с изначальным веденным размером матрицы'''
        if len(other.matrix) == self.rows:
            if len(other.matrix[0]) == self.columns:
                return True
            else:
                print('Вы ввели значения в колонках матрицы, которые не соответсвуют размеру матрицы')
                return False
        else:
            print('Вы ввели значения в строках матрицы, которые не соответсвуют размеру матрицы')
            return False


    def add_matrix(self, other):
        '''Метод по сложению матриц'''

        result = np.zeros((len(self.matrix), len(self.matrix[0])), dtype='int')

        if self._check_input_value_for_matrix(other=other):
            # Алгоритм по сложению чисел в матрицах (1-ая ячейка 1-ой матрицы складывается с 1-ой ячейкой
            # 2-ой матрицы)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        else:
            print('Ошибка в вводе значений матриц')

        return result



    def subtraction_matrix(self, other):
        '''Метод по вычитанию матриц'''

        result = np.zeros((len(self.matrix), len(self.matrix[0])), dtype='int')

        if self._check_input_value_for_matrix(other=other):
            # Алгоритм по вычитанию чисел в матрицах (1-ая ячейка 1-ой матрицы вычитается с 1-ой ячейкой
            # 2-ой матрицы
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]

        else:
            print('Ошибка в вводе значений матриц')

        return result



    def multi_matrix(self, other):
        '''Метод по умножению матриц'''

        result = np.zeros((len(self.matrix), len(self.matrix[0])), dtype='int')

        if self.rows == other.columns:
            if self.columns == other.rows:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        result[i][j] = self.matrix[i][j] * other.matrix[j][i]

            else:
                print('Ошибка в вводе значений матриц')

        return result



    def transposition_matrix(self):
        '''Метод по транспонированию матрицы'''

        result = np.zeros((self.columns, self.rows), dtype='int')
        # Проверка введеных значений в матрицу
        if len(self.matrix) == self.rows:
            if len(self.matrix[0]) == self.columns:
                # Алгоритм по транспонированию матрицы
                for i in range(self.columns):
                    for j in range(self.rows):
                        result[i][j] = self.matrix[j][i]

            else:
                print('Вы ввели значения в колонках матрицы, которые не соответсвуют размеру матрицы')
        else:
            print('Вы ввели значения в строках матрицы, которые не соответсвуют размеру матрицы')

        return result



if __name__ == '__main__':
    m1 = Matrix(rows=2, columns=3)
    m1.matrix = [[1, 2, 3], [4, 5, 6]]

    m2 = Matrix(rows=2, columns=3)
    m2.matrix = [[7, 8, 9], [9, 2, 6]]

    result = m1.add_matrix(other=m2)
    result2 = m1.subtraction_matrix(other=m2)

    print("Сложение матриц")
    print(result)
    print('Вычитание матриц')
    print(result2)

    print('Транспонирование матрицы')
    print(m1.transposition_matrix())

    m3 = Matrix(rows=3, columns=2)
    m3.matrix = [[2, 3], [5, 7], [9, 6]]

    result3 = m3.multi_matrix(other=m1)
    print('Умножение матриц')
    print(result3)
