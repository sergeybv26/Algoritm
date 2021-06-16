"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array_original = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array_original}')

first_min_element = MAX_ITEM

max_element = MIN_ITEM

for i in array_original:
    if i >= max_element:
        max_element = i
    if i <= first_min_element:
        first_min_element = i

second_min_element = max_element

if array_original.count(first_min_element) > 1:
    second_min_element = first_min_element
else:
    for i in array_original:
        if first_min_element < i < second_min_element:
            second_min_element = i

print(f'Первый наименьший элемент: {first_min_element}')
print(f'Второй наименьший элемент: {second_min_element}')
