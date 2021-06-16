"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

from random import randint

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array}')

max_neg_number = MIN_ITEM
max_neg_idx = 0

for i in range(len(array)):
    if 0 > array[i] > max_neg_number:
        max_neg_idx = i
        max_neg_number = array[i]

print(f'Максимальный отрицательный элемент в массиве: {max_neg_number}. Его позиция в массиве: {max_neg_idx}')
