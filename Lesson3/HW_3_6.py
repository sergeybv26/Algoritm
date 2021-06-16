"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Решил, что нужно реализовать следующий алгоритм:
Программа учитывает, что в списке может быть несколько минимальных и максимальных значений и
вычисляет сумму элементов между ближайшим минимальным и максимальным элементом
"""

from random import randint

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100

array_original = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array_original}')

max_element = MIN_ITEM
min_element = MAX_ITEM
max_element_idx = []
min_element_idx = []
idx_difference = SIZE
final_idx = [None, None]
summ_elements = 0

for i in range(len(array_original)):
    if array_original[i] >= max_element:
        max_element = array_original[i]
    if array_original[i] <= min_element:
        min_element = array_original[i]

for i in range(len(array_original)):
    if array_original[i] == max_element:
        max_element_idx.append(i)
    elif array_original[i] == min_element:
        min_element_idx.append(i)

for i in max_element_idx:
    for j in min_element_idx:
        if abs(i - j) < idx_difference:
            idx_difference = abs(i - j)
            final_idx = [i, j]

if final_idx[0] > final_idx[1]:
    final_idx[0], final_idx[1] = final_idx[1], final_idx[0]

for i in range(final_idx[0] + 1, final_idx[1]):
    summ_elements += array_original[i]

print(f'min = {min_element}')
print(f'max = {max_element}')
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами массива равна: {summ_elements}')
