"""
Третья версия реализации программы.
Оптимизируем использование памяти за счет объединения двух списков max_element_idx и min_element_idx в один
"""

from random import randint
from collections import deque
import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


"""
Для анализа добавлю  кортеж SYS_VAR, в котором содержатся переменные, не подлежащие анализу.
Например, переменная в цикле for или переменные, используемые для анализа. 
Размер таких переменных или будет добавляться к результату или не нужен для учета.
"""
SYS_VAR = ('i', 'idx', 'randint', 'show', 'sys', 'SYS_VAR', 'deque')

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100

array_original = tuple(randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))

print(f'Исходный массив: {array_original}')

max_element = MIN_ITEM
min_element = MAX_ITEM
max_min_element_idx = deque(['None'])
# min_element_idx = []
idx_difference = SIZE
final_idx = ()
summ_elements = 0
idx = SIZE

for i in range(len(array_original)):
    if array_original[i] >= max_element:
        max_element = array_original[i]
    if array_original[i] <= min_element:
        min_element = array_original[i]

for i in range(len(array_original)):
    if array_original[i] == max_element:
        max_min_element_idx.append(i)
    elif array_original[i] == min_element:
        max_min_element_idx.appendleft(i)

"""
Так как очередь в дальнейшем буду сокращать, то посмотрим объем занимаемой памяти в данном месте
"""
# print('Объем занимаемы очередью max_min_element_idx:')
# show(max_min_element_idx)

while idx != 'None':
    for i in max_min_element_idx:
        if i != 'None':
            if abs(idx - i) < idx_difference:
                idx_difference = abs(idx - i)
                final_idx = (idx, i)
                final_idx = tuple(sorted(final_idx))
    idx = max_min_element_idx.pop()

# for i in max_element_idx:
#     for j in min_element_idx:
#         if abs(i - j) < idx_difference:
#             idx_difference = abs(i - j)
#             final_idx = (i, j)
#             final_idx = tuple(sorted(final_idx))

for i in range(final_idx[0] + 1, final_idx[1]):
    summ_elements += array_original[i]

print(f'min = {min_element}')
print(f'max = {max_element}')
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами массива равна: {summ_elements}')


# Цикл для вывода информации о занимаемой памяти
for items in dir():
    if not items.startswith('__') and items not in SYS_VAR:
        print(f'Объем памяти, занимаемый переменной {items}:')
        show(globals()[items])

"""
После замены списков max_element_idx и min_element_idx на очередь объем используемой памяти значительно увеличился.
Вместо 176 байт, которые занимают собственно списки, очередь занимает 624 или 1152 байт (пробовал на разных данных).

=========================
Общий вывод

Наиболее оптимальной в плане использования памяти является вторая версия программы.
Если бы в программе использовались операции insert() в списках, то можно было бы использовать 3 версию,
для повышения производительности, но расход памяти при этом возрастает, что не отвечает требованиям задания.
Решение о применении deque было сильно ошибочным.

"""
