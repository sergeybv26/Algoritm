"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима)
"""

from random import randint, choice
from bubbles_sort_module import bubbles_sort

START_NUM = 0
END_NUM = 50
M = 10


def find_median(arr):
    """
    :param arr: массив нечетного количества чисел
    :return: число, которое является медианной массива
    """

    k = len(arr) // 2

    return quickselect(arr, k)


def quickselect(arr, k):
    """
    Осуществляет поиск k-того элемента в списке arr.
    Функция основана на алгоритме quickselect, разработанном Тони Хоаром
    :param arr: список чисел
    :param k: индекс
    :return: k-тый элемент в списке arr
    """

    if len(arr) == 1:
        return arr[0]

    pivot = choice(arr)

    low_elements = [el for el in arr if el < pivot]
    hight_elements = [el for el in arr if el > pivot]
    pivot_elements = [el for el in arr if el == pivot]
    len_low = len(low_elements)
    len_pivots = len(pivot_elements)

    if k < len_low:
        return quickselect(low_elements, k)
    elif k < len_low + len_pivots:
        return pivot_elements[0]
    else:
        return quickselect(hight_elements, k - len_low - len_pivots)


size = 2 * M + 1

array = [randint(START_NUM, END_NUM) for _ in range(size)]
print(f'Исходный массив:\n{array}')
median = find_median(array)
print(f'\nМедиана: {median}\n')

"""
Для проверки правильности вывода медианы выполним сортировку ранее 
написанным методом "пузырька" 
"""
print('Проверка правильности определения медианы')
sorted_array = bubbles_sort(array)
print(f'\nОтсортированный массив:\n{sorted_array}')
if median == sorted_array[len(sorted_array) // 2]:
    print('\nМедиана определена верно')
else:
    print('\nГде-то закралась ошибка')
