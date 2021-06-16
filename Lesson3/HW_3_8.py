"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROW = 5
COLUMN = 4

matrix = []

for i in range(ROW):
    elem_matrix = []
    summ_elements = 0
    for j in range(COLUMN - 1):
        elem = int(input('Введите элемент матрицы: '))
        elem_matrix.append(elem)
    for j in elem_matrix:
        summ_elements += j
    elem_matrix.append(summ_elements)
    matrix.append(elem_matrix)

for i in range(ROW):
    for j in range(COLUMN):
        print(matrix[i][j], end='\t')
    print()

