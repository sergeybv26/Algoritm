"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


from collections import deque


NUM_DEC_HEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3',
               4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D',
               14: 'E', 15: 'F'}

num_1 = list(input('Введите первое число: ').upper())
num_2 = list(input('Введите второе число: ').upper())


# Вычисление суммы чисел

def summ_hex(num_1_, num_2_):
    """

    :param num_1_: коллекция, содержащая очередь из разрядов шестнадцатиричного числа
    :param num_2_: коллекция, содержащая очередь из разрядов шестнадцатиричного числа
    :return: список, содержащий результат суммы шестнадцатиричных чисел
    """
    transfer_ = 0
    summ_hex_ = deque()

    if len(num_1_) > len(num_2_):
        num_1_, num_2_ = deque(num_1_), deque(num_2_)
    else:
        num_1_, num_2_ = deque(num_2_), deque(num_1_)

    while num_1_:
        if num_2_:
            temp = NUM_DEC_HEX[num_1_.pop()] + NUM_DEC_HEX[num_2_.pop()] + transfer_
        else:
            temp = NUM_DEC_HEX[num_1_.pop()] + transfer_

        transfer_ = 0

        if temp >= 16:
            summ_hex_.appendleft(NUM_DEC_HEX[temp - 16])
            transfer_ = 1
        else:
            summ_hex_.appendleft(NUM_DEC_HEX[temp])

    if transfer_ == 1:
        summ_hex_.appendleft(NUM_DEC_HEX[transfer_])

    return summ_hex_


# Вычисление произведения чисел

def mult_hex(num_1_, num_2_):
    """
    :param num_1_: коллекция, содержащая очередь из разрядов шестнадцатиричного числа
    :param num_2_: коллекция, содержащая очередь из разрядов шестнадцатиричного числа
    :return: список, содержащий результат произведения шестнадцатиричных чисел
    """

    transfer = 0
    count = 0
    temp_result = [deque() for _ in range(len(num_2_))]
    mult_hex_ = deque()

    while num_2_:
        digit = NUM_DEC_HEX[num_2_.pop()]
        for i in range(len(num_1_) - 1, -1, -1):
            temp = digit * NUM_DEC_HEX[num_1_[i]] + transfer
            transfer = 0
            if temp < 16:
                temp_result[count].appendleft(NUM_DEC_HEX[temp])
            else:
                temp_result[count].appendleft(NUM_DEC_HEX[temp % 16])
                transfer = temp // 16
            if transfer > 0 and i == 0:
                temp_result[count].appendleft(NUM_DEC_HEX[transfer])
        if count > 0:
            for _ in range(count):
                temp_result[count].append('0')

        count += 1

    for i in temp_result:
        mult_hex_ = summ_hex(mult_hex_, i)

    return mult_hex_


print('Результат сложения введенных чисел: ', end='')
print(*list(summ_hex(num_1, num_2)), sep='')

print('Результат произведения введенных чисел: ', end='')
print(*list(mult_hex(num_1, num_2)), sep='')
