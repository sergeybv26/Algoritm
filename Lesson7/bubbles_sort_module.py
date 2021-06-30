"""
Осуществляет сортировку массива чисел "пузырьковым" методом
"""


def bubbles_sort(arr):
    """
    :param arr: На вход подается не сортированный список чисел
    :return: Возвращает отсортированный список
    """
    len_array = len(arr)
    n = 1

    while n < len_array:
        flag = 0
        for i in range(len_array - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1
        if not flag:
            break
        n += 1
    return arr
