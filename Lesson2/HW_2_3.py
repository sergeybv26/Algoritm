"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def mirroring_number(n):
    """
    :param n: На вход подается число
    :return: Возвращает строку, содержащую поступившее число, записанное в обратном порядке
    """

    if len(str(n)) > 1:
        remainder = n % 10
        return str(remainder) + str(mirroring_number(n // 10))
    else:
        return str(n)


number = int(input('Введите число: '))

print(mirroring_number(number))
