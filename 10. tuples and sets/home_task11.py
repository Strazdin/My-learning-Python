# Тема: Кортежи, множества, словари. Часть 1

""" Задание 1
Есть три кортежа целых чисел необходимо найти 
элементы, которые есть во всех кортежах. """

# Функция min_len_tuple принимает три кортежа в качестве параметров и возвращает список с этими кортежами в котором первый элемент - кортеж с МИНИМАЛЬНОЙ длинной
# Немного решил заморочиться... 
def min_len_tuple(tuple1, tuple2, tuple3) -> list:
  if len(tuple1) <= len(tuple2) and len(tuple1) <= len(tuple3):
    return [tuple1, tuple2, tuple3]
  elif len(tuple2) <= len(tuple1) and len(tuple2) <= len(tuple3):
    return [tuple2, tuple1, tuple3]
  return [tuple3, tuple1, tuple2]

def find_general_int_in_tuple(tuple1, tuple2, tuple3) -> list:
    # Данную задачу решаю с нахождением всего одной "оригинальной" общей цифры, которая помещается в список general_list.
    # Если такая же "оригинальная" цифра опять встретится, она уже не будет помещаться в этот список

    general_ints = []
    tuples_length_graduation = min_len_tuple(tuple1, tuple2, tuple3)

    # Наверное, получилось ускорить программу, когда в цикле обрабатывается кортеж с минимальной длинной. Хотя, конечно, еще не знаю каким образом работает оператор in, может быть и не стоило заморачиваться и обрабатывать любой кортеж не важно с какой длинной?

    for i in tuples_length_graduation[0]:
        if i in tuples_length_graduation[1] and i in tuples_length_graduation[2] and i not in general_ints:
          general_ints.append(i)
    
    return general_ints
   
import random

tuple_int_1 = tuple(random.randint(0, 300) for _ in range(random.randint(100, 1000)))
tuple_int_2 = tuple(random.randint(0, 300) for _ in range(random.randint(100, 1000)))
tuple_int_3 = tuple(random.randint(0, 300) for _ in range(random.randint(100, 1000)))
print('Задание 1: ')
print('Три кортежа: ')
print(tuple_int_1)
print('\n')
print(tuple_int_2)
print('\n')
print(tuple_int_3)
print('\nОтвет: ')
list_general_ints = find_general_int_in_tuple(tuple_int_1, tuple_int_2, tuple_int_3)

if not list_general_ints:
   print('Кортежи не имеют общих чисел')
else:
   print('Общие числа: ')
   print(*list_general_ints, sep=', ')

# Далее решил решить задачу через множества и сделать проверку. 
# Записал в переменные множеств те же самые числа, что были в кортежах
set1 = set(tuple_int_1)
set2 = set(tuple_int_2)
set3 = set(tuple_int_3)
set_general = set1 & set2 & set3
# перевел все в один тип данных
list_set_general = list(set_general)
# отсортировал навсякий
list_set_general.sort()
list_general_ints.sort()
print('\n\n\n')
# print(list_set_general)
print('\n')
# print(list_general_ints)
# Проверка
if list_set_general == list_general_ints:
    print('!!!!!!!!!!!!!РЕЗУЛЬТАТ СОВПАЛ!!!!!!!!!!!!!')

""" Задание 2
Есть три кортежа целых чисел необходимо найти 
элементы, которые уникальны для каждого списка. """
# Три кортежа взяты из задания 1
def get_uniq(tuple):
    set1 = set()
    set2 = set()
    for number in tuple:
        if number not in set1:
            set1.add(number)
        else:
            set2.add(number)

    return [number for number in tuple if number in set1 - set2]

print('Задание 2: ')
print('\nОтвет (Если ответ пуст, значит уникальных элементов не нашлось): ')
print('Первый кортеж: ')
print(*get_uniq(tuple_int_1), sep = ', ')
print('Второй кортеж: ')
print(*get_uniq(tuple_int_2), sep = ', ')
print('Третий кортеж: ')
print(*get_uniq(tuple_int_3), sep = ', ')
print('\n')

""" Задание 3
Есть три кортежа целых чисел необходимо найти эле-
менты, которые есть в каждом из кортежей и находятся 
в каждом из кортежей на той же позиции. """

# Закомментированные кортежи были нужны для тестирования...
""" tuple_int_1 = (2233,2,2,2,2,5)
tuple_int_2 = (77,2,44,5,66,666,999)
tuple_int_3 = (1,2,3,4,5) """

print('Здание 3: ')
# Нашел решение в одну строку...
print(*(x for x, y, z in zip(tuple_int_1, tuple_int_2, tuple_int_3) if x == y == z))
print('Ответ (если ответ пуст, возможно, значит, таких элементов не существует): ')
# Потом понял идею и написал свое решение:
# Тут использую функцию из задания 1; сгенерированные кортежи так же были взяты из задания 1, хотя для частоты появления совпадений лучше сбавить диапазон рандома... (для тестирования я сбавляю на 3-ем задании и прибавляю на втором)

tuples_length_graduation = min_len_tuple(tuple_int_1, tuple_int_2, tuple_int_3)

for i in range(len(tuples_length_graduation[0])):
    if tuples_length_graduation[0][i] == tuples_length_graduation[1][i] and tuples_length_graduation[0][i] == tuples_length_graduation[2][i]:
        print(tuples_length_graduation[0][i])
 