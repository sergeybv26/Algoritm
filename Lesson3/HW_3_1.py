"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


START_RANGE = 2
END_RANGE = 99
START_DIVIDER = 2
END_DIVIDER = 9

count = 0

dividend_list = [i for i in range(START_RANGE, END_RANGE + 1)]
divider_list = [i for i in range(START_DIVIDER, END_DIVIDER + 1)]

for i in divider_list:
    for j in dividend_list:
        if j % i == 0:
            count += 1
    print(f'Числу {i} кратны {count} чисел из диапазона от {START_RANGE} до {END_RANGE}')
    count = 0

"""
PS Списки можно было бы и не создавать, а просто пройтись по диапазонам чисел,
но мне кажется так нагляднее получается.

Если без списков, то код будет следующий:
START_RANGE = 2
END_RANGE = 99
START_DIVIDER = 2
END_DIVIDER = 9

count = 0

for i in range(START_RANGE, END_RANGE + 1):
    for j in range(START_DIVIDER, END_DIVIDER + 1):
        if j % i == 0:
            count += 1
    print(f'Числу {i} кратны {count} чисел из диапазона от {START_RANGE} до {END_RANGE}')
    count = 0
"""