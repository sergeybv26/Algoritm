"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы
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

max_element = 0

for i in range(ROW):
    for j in range(COLUMN):
        if matrix[i][j] >= max_element:
            max_element = matrix[i][j]

min_element = max_element
min_list = []

for i in range(COLUMN):
    for j in range(ROW):
        if matrix[j][i] < min_element:
            min_element = matrix[j][i]
    min_list.append(min_element)
    min_element = max_element

print(*matrix, sep='\n')
print()

max_element = 0

for i in min_list:
    if i > max_element:
        max_element = i

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы равен: {max_element}')
