"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


FIRST_ELEMENT = 1
DENOMINATOR = -0.5


def summ_geometric_progression(b, q, cnt, quantity):
    """
    :param b: n-ый элемент геометрической прогрессии
    :param q: знаменатель геометрической прогресии
    :param cnt: порядковый номер элемента
    :param quantity: количество элементов геометрической прогресси
    :return: возвращает сумму элементов прогрессии
    """

    if cnt <= quantity:
        if cnt == 1:
            cnt += 1
            return summ_element + b + summ_geometric_progression(b, q, cnt, quantity)
        else:
            cnt += 1
            b *= q
            return summ_element + b + summ_geometric_progression(b, q, cnt, quantity)
    else:
        return summ_element + 0


n = int(input('Введите количество элементов: '))

count = 1
summ_element = 0

print(summ_geometric_progression(FIRST_ELEMENT, DENOMINATOR, count, n))


"""
Решение без циклов для проверки
"""

summ_element = FIRST_ELEMENT * (pow(DENOMINATOR, n) - 1) / (DENOMINATOR - 1)

print(f'Сумма, полученная при расчете по формуле: {summ_element}')
