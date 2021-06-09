if __name__ == '__main__':

    import random

    """
    Написать программу, которая генерирует в указанных пользователем границах:
        случайное целое число;
        случайное вещественное число;
        случайный символ.
    Для каждого из трех случаев пользователь задает свои границы диапазона. 
    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
    """

    print('Что вы хотите получить?\n1. Случайное целое число\n2. Случайное вещественное число\n3. Случайный символ')
    choice = int(input('Введите 1, 2 или 3: '))

    if choice == 1:
        print('Генерация случайного целого числа')
        number_1 = int(input('Введите первое число диапазона генерации: '))
        number_2 = int(input('Введите второе число диапазона генерации: '))

        if number_1 < number_2:
            print(f'Случайное целое число из диапазона {number_1} - {number_2}: {random.randint(number_1, number_2)}')
        else:
            print(f'Случайное целое число из диапазона {number_2} - {number_1}: {random.randint(number_2, number_1)}')

    elif choice == 2:
        print('Генерация случайного вещественного числа')
        number_1 = float(input('Введите первое число диапазона генерации: '))
        number_2 = float(input('Введите второе число диапазона генерации: '))

        if number_1 < number_2:
            print(f'Случайное целое число из диапазона {number_1} - {number_2}: {random.uniform(number_1, number_2)}')
        else:
            print(f'Случайное целое число из диапазона {number_2} - {number_1}: {random.uniform(number_2, number_1)}')

    elif choice == 3:
        char_1 = input('Введите первый символ диапазона генерации: ')
        char_2 = input('Введите второй символ диапазона генерации: ')

        char_1_num = ord(char_1)
        char_2_num = ord(char_2)

        if char_1_num < char_2_num:
            rand_char = random.randint(char_1_num, char_2_num)
            print(f'Случайный символ из диапазона {char_1} - {char_2}: {chr(rand_char)}')
        else:
            rand_char = random.randint(char_2_num, char_1_num)
            print(f'Случайный символ из диапазона {char_2} - {char_1}: {chr(rand_char)}')

    else:
        print('Неверный выбор желаемого результата')
