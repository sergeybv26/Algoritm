"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array}')

max_element_idx = []
min_element_idx = []
max_element = MIN_ITEM
min_element = MAX_ITEM

# Находим значение максимального и минимального элементов
for i in array:
    if i > max_element:
        max_element = i
    if i < min_element:
        min_element = i

# Находим индексы максимальных и минимальных элементов
for i in range(len(array)):
    if array[i] == max_element:
        max_element_idx.append(i)
    elif array[i] == min_element:
        min_element_idx.append(i)

# Сравниваем количество индексов максимальных и минимальных элементов и уравниваем их
while len(max_element_idx) != len(min_element_idx):
    if len(max_element_idx) > len(min_element_idx):
        max_element_idx.pop()
    else:
        min_element_idx.pop()

# Обмениваем значения максимальных и минимальных элементов
for i in range(len(max_element_idx)):
    array[max_element_idx[i]], array[min_element_idx[i]] = array[min_element_idx[i]], array[max_element_idx[i]]

print(f'Результирующий массив: {array}')
