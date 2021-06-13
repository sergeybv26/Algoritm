"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
"""

number = int(input('Введите натуральное число: '))

even_num_quantity = 0
odd_num_quantity = 0

while number > 0:
    remainder = number % 10

    if remainder % 2 == 0:
        even_num_quantity += 1
    else:
        odd_num_quantity += 1

    number = number // 10

print(f'Количество четных цифр: {even_num_quantity}')
print(f'Количество нечетных цифр: {odd_num_quantity}')
