"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    number_1 = float(input('Введите первое число: '))
    operation_smb = input('Введите знак операции (Для завершения работы введите 0): ')
    number_2 = float(input('Введите второе число: '))

    while (operation_smb != '0' and operation_smb != '+' and operation_smb != '-'
           and operation_smb != '*' and operation_smb != '/'):
        print('Введен неверный знак операции')
        operation_smb = input('Введите знак операции: ')

    if operation_smb != '0':
        if operation_smb == '+':
            result = number_1 + number_2
            print(f'{number_1:.2f} + {number_2:.2f} = {result:.2f}')
        elif operation_smb == '-':
            result = number_1 - number_2
            print(f'{number_1:.2f} - {number_2:.2f} = {result:.2f}')
        elif operation_smb == '*':
            result = number_1 * number_2
            print(f'{number_1:.2f} * {number_2:.2f} = {result:.2f}')
        elif number_2 == 0:
            print('На ноль делить нельзя!')
        else:
            result = number_1 / number_2
            print(f'{number_1:.2f} / {number_2:.2f} = {result:.2f}')
    else:
        break
