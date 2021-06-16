"""
Определить, какое число в массиве встречается чаще всего
"""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array}')

max_count = 0
max_number = MIN_ITEM

for i in range(len(array)):
    if array.count(array[i]) > max_count:
        max_count = array.count(array[i])
        max_number = array[i]

if max_count > 1:
    print(f'Число {max_number} встречается наибольшее количество раз - {max_count}')
else:
    print('Все числа в массиве разные и встречаются по 1 разу')
