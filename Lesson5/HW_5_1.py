"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import defaultdict


SEP_STRING = '=' * 36

qnt_firm = int(input('Введите количество предприятий: '))

firm_dict = defaultdict(float)
more_avrg = []
less_avrg = []
summ = 0

for _ in range(qnt_firm):
    name = input('Введите наименование предприятия: ')
    for i in range(4):
        profit = float(input(f'Введите прибыль за {i + 1}-й квартал: '))
        firm_dict[name] += profit
    summ += firm_dict[name]

avrg = summ / qnt_firm

for key in firm_dict:
    if firm_dict[key] >= avrg:
        more_avrg.append(key)
    else:
        less_avrg.append(key)

print('Предпиятия с прибылью выше среднего:')
print(*more_avrg, sep='\n')
print(SEP_STRING)
print('Предприятия с прибылью ниже среднего:')
print(*less_avrg, sep='\n')
