"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform

START_NUM = 0
END_NUM = 50
SIZE = 20


def merge_sort(arr):
    """
    :param arr: массив чисел
    :return: сортирует массив методом слияния
    """

    len_array = len(arr)

    if len_array == 1 or len_array == 0:
        return

    middle = len_array // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    merge_sort(left_half)
    merge_sort(right_half)

    len_left_half = len(left_half)
    len_right_half = len(right_half)
    i = 0
    j = 0
    t = 0

    while i < len_left_half and j < len_right_half:
        if left_half[i] <= right_half[j]:
            arr[t] = left_half[i]
            i += 1
        else:
            arr[t] = right_half[j]
            j += 1
        t += 1

    while i < len_left_half:
        arr[t] = left_half[i]
        i += 1
        t += 1

    while j < len_right_half:
        arr[t] = right_half[j]
        j += 1
        t += 1


array = [i for i in [round(uniform(START_NUM, END_NUM), 2) for _ in range(SIZE)] if i != 50]

print(f'Исходный массив:\n{array}')
merge_sort(array)
print(f'Отсортированный массив:\n{array}')
