"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),

● написать 3 варианта кода (один у вас уже есть),

● проанализировать 3 варианта и выбрать оптимальный,

● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),

● написать общий вывод: какой из трёх вариантов лучше и почему.

==============================================
Для проведения анализа взял 3 задачу 3 урока
==============================================
"""


from random import randint
from timeit import timeit
import cProfile

"""
Для проведения анализа в исходный код добавлю функции
"""
SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000


def array_create(min_item_, max_item_, size_):
    array_ = [randint(min_item_, max_item_) for _ in range(size_)]
    # print(f'Исходный массив: {array_}')
    return array_


# Находим значение максимального и минимального элементов
# def max_min_find(array_, min_element_, max_element_):
#     for elem in array_:
#         if elem > max_element_:
#             max_element_ = elem
#         if elem < min_element_:
#             min_element_ = elem
#     return max_element_, min_element_


# Находим индексы максимальных и минимальных элементов
# def max_min_idx(array_, max_element_, min_element_):
#     max_element_idx_ = []
#     min_element_idx_ = []
#     for idx in range(len(array_)):
#         if array_[idx] == max_element_:
#             max_element_idx_.append(idx)
#         elif array_[idx] == min_element_:
#             min_element_idx_.append(idx)
#     return max_element_idx_, min_element_idx_


# Сравниваем количество индексов максимальных и минимальных элементов и уравниваем их
# def comparison_idx(max_element_idx_, min_element_idx_):
#     while len(max_element_idx_) != len(min_element_idx_):
#         if len(max_element_idx_) > len(min_element_idx_):
#             max_element_idx_.pop()
#         else:
#             min_element_idx_.pop()
#     return max_element_idx_, min_element_idx_


# Обмениваем значения максимальных и минимальных элементов
# def change_elements(array_, max_elem_idx_, min_elem_idx_):
#     for idx in range(len(max_elem_idx_)):
#        array_[max_elem_idx_[idx]], array_[min_elem_idx_[idx]] = array_[min_elem_idx_[idx]], array_[max_elem_idx_[idx]]
#     return array_


# Добавляю главную функцию
# def main(min_item_, max_item_, size_):
#     max_element = min_item_
#     min_element = max_item_
#     array = array_create(min_item_, max_item_, size_)
#     max_element, min_element = max_min_find(array, min_element, max_element)
#     max_element_idx, min_element_idx = max_min_idx(array, max_element, min_element)
#     max_element_idx, min_element_idx = comparison_idx(max_element_idx, min_element_idx)
#     array = change_elements(array, max_element_idx, min_element_idx)
#
#     # print(f'Результирующий массив: {array}')
#     return array


# main(MIN_ITEM, MAX_ITEM, SIZE)

# for i in range(10):
#    print(f'{SIZE ** i}\t{timeit(f"main({MIN_ITEM}, {MAX_ITEM}, {SIZE ** i})", number=100, globals=globals())}')

# cProfile.run(f'main({MIN_ITEM}, {MAX_ITEM}, {SIZE ** 6})')

"""
Время выполнения программы в зависимости от размера исходного массива:
1	    0.0035636
10	    0.003100400000000003
100	    0.031576999999999994
1000	0.3541937
10000	2.4322716
100000	35.3754538
1000000	272.8902765

При увеличении количества элементов массива в 10 раз, время выполнения также вырастает примерно в 10 раз.

 5024543 function calls in 4.173 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.030    0.030    4.173    4.173 <string>:1(<module>)
        1    0.000    0.000    3.774    3.774 HW_4_1.py:35(array_create)
        1    0.553    0.553    3.774    3.774 HW_4_1.py:36(<listcomp>)
        1    0.126    0.126    0.126    0.126 HW_4_1.py:42(max_min_find)
        1    0.243    0.243    0.243    0.243 HW_4_1.py:52(max_min_idx)
        1    0.000    0.000    0.000    0.000 HW_4_1.py:64(comparison_idx)
        1    0.000    0.000    0.000    0.000 HW_4_1.py:74(change_elements)
        1    0.000    0.000    4.143    4.143 HW_4_1.py:81(main)
  1000000    1.304    0.000    2.519    0.000 random.py:200(randrange)
  1000000    0.702    0.000    3.221    0.000 random.py:244(randint)
  1000000    0.833    0.000    1.215    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    4.173    4.173 {built-in method builtins.exec}
       60    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      990    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
  1000000    0.166    0.000    0.166    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1023469    0.216    0.000    0.216    0.000 {method 'getrandbits' of '_random.Random' objects}
       14    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

В результате выполнения cProfile видно, что наибольшее время занимает функция генерации случайных чисел.
Для дальнейшего анализа считаю необходимым выделить отдельно от основной функции генерацию первоначального массива,
так как повлиять на функцию генерации случайного числа я не могу.
"""

array = []
for pwr_size in range(7):
    array.append(array_create(MIN_ITEM, MAX_ITEM, SIZE ** pwr_size))


# def main(min_item_, max_item_, array_):
#     max_element = min_item_
#     min_element = max_item_
#     max_element, min_element = max_min_find(array_, min_element, max_element)
#     max_element_idx, min_element_idx = max_min_idx(array_, max_element, min_element)
#     max_element_idx, min_element_idx = comparison_idx(max_element_idx, min_element_idx)
#     array_ = change_elements(array_, max_element_idx, min_element_idx)
#
#     # print(f'Результирующий массив: {array}')
#     return array_


# for i in array:
#     print(f'{len(i)}\t{timeit(f"main({MIN_ITEM}, {MAX_ITEM}, {i})", number=100, globals=globals())}')

# cProfile.run(f'main({MIN_ITEM}, {MAX_ITEM}, {array[6]})')

"""
Зависимость времени выполнения от количества элементов не изменилась: при увеличении количества элементов в 10 раз,
время выполнения возрастает в 10 раз.

1	    0.0006534000000000262
10	    0.0007820999999998968
100	    0.004699999999999704
1000	0.0404618000000001
10000	0.4001505999999999
100000	4.1544383
1000000	41.5654794

  1026 function calls in 5.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.040    0.040    0.399    0.399 <string>:1(<module>)
        1    0.000    0.000    0.359    0.359 HW_4_1.py:147(main)
        1    0.124    0.124    0.124    0.124 HW_4_1.py:42(max_min_find)
        1    0.234    0.234    0.234    0.234 HW_4_1.py:52(max_min_idx)
        1    0.000    0.000    0.000    0.000 HW_4_1.py:64(comparison_idx)
        1    0.000    0.000    0.000    0.000 HW_4_1.py:74(change_elements)
        1    4.619    4.619    5.018    5.018 {built-in method builtins.exec}
       28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      984    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

При анализе видно, что по списку дважды проходимся: 1 раз при поиске элементов, второй раз при поиске индексов.
Попробуем оптимизировать это время.
"""


"""
===============================================================
Следующая версия программы. Изменяем только необходимые функции
===============================================================
"""


# def max_min_find(array_, min_element_, max_element_):
#     for elem in array_:
#         if elem > max_element_:
#             max_element_ = elem
#         if elem < min_element_:
#             min_element_ = elem
#     return max_element_, min_element_


def change_elements(array_, max_elem_, min_elem_):
    for idx, elem in enumerate(array_):
        if elem == max_elem_:
            array_[idx] = min_elem_
        elif elem == min_elem_:
            array_[idx] = max_elem_
    return array_


# def main(min_item_, max_item_, array_):
#     max_element = min_item_
#     min_element = max_item_
#     max_element, min_element = max_min_find(array_, min_element, max_element)
#     array_ = change_elements(array_, max_element, min_element)
#
#     # print(f'Результирующий массив: {array}')
#     return array_


# for i in array:
#     print(f'{len(i)}\t{timeit(f"main({MIN_ITEM}, {MAX_ITEM}, {i})", number=100, globals=globals())}')

# cProfile.run(f'main({MIN_ITEM}, {MAX_ITEM}, {array[6]})')

"""
В данной реализации тенденция нарастания времени выполнения не изменилась, но время немного уменьшилось.
Проверено при помощи нескольких запусков программы

1	    0.00025029999999981456
10	    0.00048570000000003333
100	    0.0031110999999999223
1000	0.03265460000000031
10000	0.35327870000000017
100000	3.7912518
1000000	36.79365

         6 function calls in 4.750 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.041    0.041    0.394    0.394 <string>:1(<module>)
        1    0.140    0.140    0.140    0.140 HW_4_1.py:203(max_min_find)
        1    0.213    0.213    0.213    0.213 HW_4_1.py:212(change_elements)
        1    0.000    0.000    0.353    0.353 HW_4_1.py:221(main)
        1    4.356    4.356    4.750    4.750 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Исключение лишнего обхода массива позволило немного сократить время выполнения.
В дальнейшей реализации планирую заменить самописную функцию поиска минимального и максимального значения
на встроенные, а затем выполнить замену элементов.
Возможно от этого будет какой-то результат... 
"""

"""
===============================================================
Следующая версия программы. Изменяем только необходимые функции
===============================================================
"""


def max_min_find(array_):
    max_element_ = max(array_)
    min_element_ = min(array_)

    return max_element_, min_element_


def main(array_):
    max_element, min_element = max_min_find(array_)
    for idx, elem in enumerate(array_):
        if elem == max_element:
            array_[idx] = min_element
        elif elem == min_element:
            array_[idx] = max_element

    # print(f'Результирующий массив: {array}')
    return array_


for i in array:
    print(f'{len(i)}\t{timeit(f"main({i})", number=100, globals=globals())}')


cProfile.run(f'main({array[6]})')

"""
Тенденция и время выполнения в данной реализации программы практически не изменились от предыдущих результатов.

1	0.0001509999999997902
10	0.00038559999999998595
100	0.0024784000000002138
1000	0.028686999999999685
10000	0.3124121999999998
100000	3.4112223
1000000	30.6472085

         7 function calls in 4.777 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.039    0.039    0.295    0.295 <string>:1(<module>)
        1    0.000    0.000    0.068    0.068 HW_4_1.py:276(max_min_find)
        1    0.188    0.188    0.256    0.256 HW_4_1.py:283(main)
        1    4.483    4.483    4.777    4.777 {built-in method builtins.exec}
        1    0.034    0.034    0.034    0.034 {built-in method builtins.max}
        1    0.034    0.034    0.034    0.034 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Не совсем понятно почему общее время выполнения осталось таким же, так как судя 
по отчету cProfile в последней реализации программа отработала на 100 мс быстрее, если смотреть на время выполнения
функции main. Видимо все равно учитывается время создания массива, несмотря на то, что он создается отдельно
от функции main. 
"""

"""
==================================================================
Общий вывод
Если анализировать время выполнения по функции main, то самая быстрая реализация - это последняя.
(видимо встроенные функции max и min работают побыстрее, чем мои)

Какой-то в корне другой алгоритм я придумать не смог, так как решение задачи, если смотреть глобально, сводится
к следующим шагам:
    - определение минимального и максимального значения в списке
    - размен местами максимального и минимального значения

Тенденция роста времени в зависимости от размера исходного массива не изменяется во всех реализациях:
при увеличении размера массива в 10 раз - время увеличивается в 10 раз.
Таким образом зависимость времени выполнения от количества элементов имеет вид прямой. Однако, возможно при 
еще больших размерах массива будет резкий нелинейный рост времени выполнения, так как процессор не сможет 
разместить число в регистре за один раз.

==================================================================
"""