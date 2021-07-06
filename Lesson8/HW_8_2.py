"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Задание вызвало сложность. Пришлось много "гуглить". Начитался, что лучше всего данную задачу решать
через очередь с приоритетом, так и сделал.
"""

import heapq
from collections import Counter
from itertools import count


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code_, prefix):
        self.left.walk(code_, prefix + '0')
        self.right.walk(code_, prefix + '1')


class Leaf:

    def __init__(self, char):
        self.char = char

    def walk(self, code_, prefix):
        code_[self.char] = prefix


def encode(string):
    temp_list = []
    temp_count = count()  # добавлен в очередь кучи для исключения ошибки сравнения при равных приоритетах
    for char, freq in Counter(string).items():
        temp_list.append((freq, next(temp_count), Leaf(char)))

    heapq.heapify(temp_list)

    while len(temp_list) > 1:
        freq1, _count1, left = heapq.heappop(temp_list)
        freq2, _count2, right = heapq.heappop(temp_list)

        heapq.heappush(temp_list, (freq1 + freq2, next(temp_count), Node(left, right)))

    smb_code = {}

    root = temp_list[0][2]
    root.walk(smb_code, "")

    return smb_code


def decode(encoded_, code_):
    decoded_list = []
    encod_char = ''
    for char in encoded_:
        encod_char += char
        for dec_char in code_:
            if code_.get(dec_char) == encod_char:
                decoded_list.append(dec_char)
                encod_char = ''
                break
    return ''.join(decoded_list)


user_string = input('Введите строку: ')
# user_string = 'fhksjhkjsh dkafjhdkjhfk adkjhfkjahfkj'

code = encode(user_string)

encoded = "".join(code[char] for char in user_string)
print('Таблица кодов:')
for char in sorted(code):
    print(f'{char}: {code[char]}')

print(f'Закодированная строка: {encoded}')

decoded = decode(encoded, code)

print(f'Декодированная строка: {decoded}')
if decoded == user_string:
    print('Закодированная строка после декодирования совпадает с исходной')
else:
    print('Ошибка!')
