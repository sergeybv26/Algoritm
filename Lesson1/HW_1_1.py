if __name__ == '__main__':

    """
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
    """

    number = int(input('Введите трехзначное число: '))

    digit1 = number % 10
    number = number // 10
    digit2 = number % 10
    digit3 = number // 10

    print(f'Сумма чисел равна: {digit1 + digit2 + digit3}')
    print(f'Произведение чисел равно: {digit1 * digit2 * digit3}')
