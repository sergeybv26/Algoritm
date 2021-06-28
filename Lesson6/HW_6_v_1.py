"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.

===================================================

ОС: Windows 10 64 bit
Python 3.8.7

===================================================
Для выполнения задания взял 6 задачу 3 урока
===================================================

Проведем анализ использования памяти в исходной версии программы

"""


from random import randint
import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


"""
Для анализа добавлю  кортеж SYS_VAR, в котором содержатся переменные, не подлежащие анализу.
Например, переменная в цикле for или переменные, используемые для анализа. 
Размер таких переменных или будет добавляться к результату или не нужен для учета.
"""
SYS_VAR = ('i', 'j', 'randint', 'show', 'sys', 'SYS_VAR')

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100

array_original = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: {array_original}')

max_element = MIN_ITEM
min_element = MAX_ITEM
max_element_idx = []
min_element_idx = []
idx_difference = SIZE
final_idx = [None, None]
summ_elements = 0

for i in range(len(array_original)):
    if array_original[i] >= max_element:
        max_element = array_original[i]
    if array_original[i] <= min_element:
        min_element = array_original[i]

for i in range(len(array_original)):
    if array_original[i] == max_element:
        max_element_idx.append(i)
    elif array_original[i] == min_element:
        min_element_idx.append(i)

for i in max_element_idx:
    for j in min_element_idx:
        if abs(i - j) < idx_difference:
            idx_difference = abs(i - j)
            final_idx = [i, j]

if final_idx[0] > final_idx[1]:
    final_idx[0], final_idx[1] = final_idx[1], final_idx[0]

for i in range(final_idx[0] + 1, final_idx[1]):
    summ_elements += array_original[i]

print(f'min = {min_element}')
print(f'max = {max_element}')
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами массива равна: {summ_elements}')


# Цикл для вывода информации о занимаемой памяти
for items in dir():
    if not items.startswith('__') and items not in SYS_VAR:
        print(f'Объем памяти, занимаемый переменной {items}:')
        show(globals()[items])


"""
Так как числа формируются в случайном порядке, больше двух одинаковых максимальных или минимальных значений добиться
не удалось. Выполнил подсчет объема используемой памяти при наличии в исходном списке двух минимальных элементов.
Объем памяти составил 4344 байта.

========================
Итог на настоящий момент

В программе имеются списки, которые в процессе работы не изменяются, поэтому имеет смысл заменить их на кортежи,
это позволит сэкономить немного памяти. Этим и займемся во 2 версии программы.

Итоговый вывод напишу в 3-ей версии программы

=======================

PS Сделал попытку автоматического подсчета количества используемой памяти в функции show(), но что-то пошло не так, 
подсчет велся не верно... Разобраться в причинах так и не смог. Поэтому делал на калькуляторе :)
Приведу код функции show() и цикла вывода данных, может подскажете что у меня не так?
Получается с рекурсией нужно еще поразбираться, слабые у меня знания. А может нужно попозже взглянуть на задачу,
у меня такое бывает, что сидишь и ничего не получается, а потом делаешь перерыв и видишь, что все просто же.

def show(obj, summ_memory_):
    summ_memory += sys.getsizeof(obj)
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key, summ_memory_)
                show(value, summ_memory_)
        else:
            for item in obj:
                show(item, summ_memory_)
    return summ_memory_

memory = 0    
for items in dir():
    summ_memory = 0
    if not items.startswith('__') and items not in SYS_VAR:
        print(f'Объем памяти, занимаемый переменной {items}:')
        memory += show(globals()[items])



Для информации приведу вывод после работы цикла:

Объем памяти, занимаемый переменной MAX_ITEM:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
Объем памяти, занимаемый переменной MIN_ITEM:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-100
Объем памяти, занимаемый переменной SIZE:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
Объем памяти, занимаемый переменной array_original:
type(obj)=<class 'list'>, sys.getsizeof(obj)=904, obj=[-9, 6, 72, -39, 40, -8, -40, 67, 56, 100, 90, 9, -21, -21, -65, 
-40, 20, 68, 57, 0, -13, 68, 41, 27, 49, 58, -95, 46, 51, -81, 66, -35, 5, 40, 81, 63, 1, 4, 24, -59, -16, -99, 72, 
-63, 50, 17, -79, -99, 19, 56, 61, 39, 59, -61, 35, 50, 27, -6, 27, 78, 83, 37, 19, 14, 14, 29, 42, -63, -50, 27, -59,
 77, 76, 68, -6, -82, -70, -6, 55, 54, -82, -76, 2, 30, -33, 72, 73, 21, 15, 58, -20, -62, 72, -28, -93, 54, -82, 12,
  -25, -2]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-9
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=6
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-39
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-8
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-40
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=67
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=90
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-21
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-21
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-65
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-40
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=20
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=68
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=57
type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-13
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=68
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=41
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=49
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=58
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-95
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=46
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=51
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-81
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=66
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-35
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=81
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=63
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=1
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-59
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-16
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-99
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-63
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=50
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=17
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-79
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-99
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=19
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=61
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=39
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=59
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-61
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=35
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=50
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-6
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=78
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=83
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=37
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=19
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=14
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=14
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=29
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-63
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-50
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-59
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=77
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=76
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=68
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-6
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-82
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-70
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-6
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=55
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-82
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-76
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-33
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=73
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=21
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=15
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=58
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-20
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-62
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-28
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-93
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-82
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-25
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-2
Объем памяти, занимаемый переменной final_idx:
type(obj)=<class 'list'>, sys.getsizeof(obj)=72, obj=[9, 41]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=41
Объем памяти, занимаемый переменной idx_difference:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=32
Объем памяти, занимаемый переменной max_element:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=100
Объем памяти, занимаемый переменной max_element_idx:
type(obj)=<class 'list'>, sys.getsizeof(obj)=88, obj=[9]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=9
Объем памяти, занимаемый переменной min_element:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=-99
Объем памяти, занимаемый переменной min_element_idx:
type(obj)=<class 'list'>, sys.getsizeof(obj)=88, obj=[41, 47]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=41
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=47
Объем памяти, занимаемый переменной summ_elements:
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=422
"""
