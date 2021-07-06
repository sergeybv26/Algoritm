"""
 Определение количества различных подстрок с использованием хэш-функции.
 Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
 Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

s = input('Введите строку: ').lower()

s_len = len(s)
s_hash = hashlib.sha1(s.encode('utf-8')).hexdigest()
count = 0
sub_s_hash_list = []

for i in range(s_len):
    for j in range(s_len, i, -1):
        sub_s_hash = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
        if sub_s_hash not in sub_s_hash_list and sub_s_hash != s_hash:
            sub_s_hash_list.append(sub_s_hash)
            count += 1

print(f'В строке {s} найдено {count} различных подстрок')
