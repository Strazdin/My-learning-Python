# Модуль 4. Строки. Списки. Часть 3

""" Задание 1
Два списка целых заполняются случайными числами. 
Необходимо: """

import random

""" 1. Сформировать третий список, содержащий элементы 
обоих списков; """

print('-------------------------------')
spisok_1 = [random.randint(1, 10) for i in range(10)]
spisok_2 = [random.randint(1, 10) for i in range(10)]
spisok_3 = spisok_1 + spisok_2
print('1. Третий список из элементов обоих списков: ')
print(spisok_3)

""" 2. Сформировать третий список, содержащий элементы 
обоих списков без повторений; """

print('-------------------------------')
spisok_1 = [random.randint(1, 10) for i in range(10)]
spisok_2 = [random.randint(1, 10) for i in range(10)]
spisok_3 = spisok_1 + spisok_2
spisok_3.sort()
print('2. Общий список: ')
print(spisok_3)

for k in spisok_3:
    count_elem = spisok_3.count(k)

    if count_elem > 1:
        for _ in range(count_elem - 1):
            spisok_3.remove(k)

print('3. Третий список, содержащий элементы обоих списков без повторений: ')
print(spisok_3)

""" 3. Сформировать третий список, содержащий элементы 
общие для двух списков; """

print('-------------------------------')
spisok_1 = [random.randint(1, 10) for i in range(10)]
spisok_2 = [random.randint(1, 10) for i in range(10)]
spisok_3 = []
spisok_1.sort()
spisok_2.sort()
print('3. Рандом списки: ')
print(spisok_1)
print(spisok_2)

for k in spisok_1:
    for j in spisok_2:
        if k == j:
            spisok_3.append(k)
            count_elem_1 = spisok_1.count(k)
            count_elem_2 = spisok_2.count(k)

            if count_elem_1 > 1:
                for _ in range(count_elem_1 - 1):
                    spisok_1.remove(j)

            if count_elem_2 > 1:
                for _ in range(count_elem_2 - 1):
                    spisok_2.remove(j)

print('Общие элементы для двух списков: ')
print(spisok_3)

""" 4. Сформировать третий список, содержащий только 
уникальные элементы каждого из списков; """

print('-------------------------------')
spisok_1 = [random.randint(1, 10) for i in range(10)]
spisok_2 = [random.randint(1, 10) for i in range(10)]
spisok_3 = []
spisok_1.sort()
spisok_2.sort()
print('4. Рандом списки: ')
print(spisok_1)
print(spisok_2)

for k in spisok_1:
    for j in spisok_2:
        if k not in spisok_2:
            if j not in spisok_1:
                spisok_3.append(k)

for n in spisok_3:
    count_elem = spisok_3.count(n)

    if count_elem > 1:
        for _ in range(count_elem - 1):
            spisok_3.remove(n)

print('Список, содержащий только уникальные элементы каждого из списков: ')
print(spisok_3)

""" 5. Сформировать третий список, содержащий только 
минимальное и максимальное значение каждого из списков"""

print('-------------------------------')
spisok_1 = [random.randint(1, 10) for i in range(10)]
spisok_2 = [random.randint(1, 10) for i in range(10)]
spisok_3 = []
spisok_1.sort()
spisok_2.sort()
print('5. Рандом списки: ')
print(spisok_1)
print(spisok_2)

spisok_3.append(min(spisok_1))
spisok_3.append(max(spisok_1))
spisok_3.append(min(spisok_2))
spisok_3.append(max(spisok_2))

print('Список, содержащий только минимальное и максимальное значение каждого из списков: ')
print(spisok_3)
