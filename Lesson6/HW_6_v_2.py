"""
Вторая версия реализации программы.
Пробуем оптимизировать использование памяти заменой некоторых списков на кортежи
"""

from random import randint
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
SYS_VAR = ('i', 'j', 'randint', 'show', 'sys', 'SYS_VAR')

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100

array_original = tuple(randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))

print(f'Исходный массив: {array_original}')

max_element = MIN_ITEM
min_element = MAX_ITEM
max_element_idx = []
min_element_idx = []
idx_difference = SIZE
final_idx = ()
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
            final_idx = (i, j)
            final_idx = tuple(sorted(final_idx))

# if final_idx[0] > final_idx[1]:
#     final_idx[0], final_idx[1] = final_idx[1], final_idx[0]

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
Выполнил преобразование списков array_original и final_idx в кортеж.
При аналогичных условиях, как и в первой версии, объем памяти составил: 4276 байт.

Имеются конечно сомнения в корректности измерений, так как в строке
final_idx = tuple(sorted(final_idx))
выполняется преобразование в список, его сортировка, а хатем обратное преобразование в кортеж.
Получается, что на время преобразования возрастает объем потребляемой памяти на 32 байта, а затем снижается


===========================
Промежуточный итог

При замене 2 списков на кортежи удалось добиться снижения объема потребления памяти на 68 байт.
Следующим этапом оптимизации вижу объединение двух списков max_element_idx и min_element_idx в один.

===========================
"""