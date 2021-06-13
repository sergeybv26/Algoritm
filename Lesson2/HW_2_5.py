"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке
"""

START_NUMBER = 32
STOP_NUMBER = 127

count_string = 1

for i in range(START_NUMBER, STOP_NUMBER + 1):
    if count_string <= 10:
        print(f'{i} - {chr(i)}')
        count_string += 1
    else:
        print()
        print(f'{i} - {chr(i)}')
        count_string = 2
