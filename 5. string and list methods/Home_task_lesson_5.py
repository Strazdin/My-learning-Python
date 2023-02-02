# Модуль 4. Строки. Списки.

""" Часть 2
Задание 1:
Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12. Необходимо вывести на экран результат выражения. 
В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция, число. Возможные операции: +, -,*,/ """

switch_variable = 0
operation = ''
arithmetic_operation_array = []
result_massage = 'Result: '

arithmetic_operation = input('Enter two integers and an arithmetic operation (+,-,/,*) between them: ').replace(' ', '')

# (Неактуально) Если пользователь ввел несколько одинаковых операций, удаляем из строки повторяющиеся операции:
# решилось проще (через обработку исключений ValueError)

""" if arithmetic_operation.count('+') > 1 or arithmetic_operation.count('-') > 1 or arithmetic_operation.count('/') > 1 or arithmetic_operation.count('*') > 1:
    for char in arithmetic_operation:
        arithmetic_operation_array.append(char)

    if '+' in arithmetic_operation_array:
        for _ in range(arithmetic_operation.count('+') - 1):
            arithmetic_operation_array.remove('+')

    if '-' in arithmetic_operation_array:
        for _ in range(arithmetic_operation.count('-') - 1):
            arithmetic_operation_array.remove('-')

    if '/' in arithmetic_operation_array:
        for _ in range(arithmetic_operation.count('/') - 1):
            arithmetic_operation_array.remove('/')

    if '*' in arithmetic_operation_array:
        for _ in range(arithmetic_operation.count('*') - 1):
            arithmetic_operation_array.remove('*')

    arithmetic_operation = ''.join(arithmetic_operation_array) """

# Когда switch_variable = 0, то ищем индекс математической операции, разбиваем строку на два числа, переводим в тип данных int
# Когда switch_variable = 1, то производим математическую операцию и записываем результат

while switch_variable < 2:
    if switch_variable == 0:
        for i in range(len(arithmetic_operation)):
            if arithmetic_operation[i] == '+' or arithmetic_operation[i] == '-' or arithmetic_operation[i] == '/' or arithmetic_operation[i] == '*':
                    index_order_operation = i
                    operation = arithmetic_operation[i]
                    try:
                        first_composed_number = int(arithmetic_operation[0:index_order_operation])
                        second_composed_number = int(arithmetic_operation[index_order_operation + 1:])
                        break
                    except ValueError:
                        switch_variable = 666
                        result_massage += 'ERROR'
                        print('Error message. The expression must consist of a single mathematical operation')
                        break
    elif switch_variable == 1:                   
        if operation == '+':
            result_arithmetic_operation = first_composed_number + second_composed_number
        elif operation == '-':
            result_arithmetic_operation = first_composed_number - second_composed_number
        elif operation == '*':
            result_arithmetic_operation = first_composed_number * second_composed_number
        else:
            try:
                result_arithmetic_operation = first_composed_number // second_composed_number
            except ZeroDivisionError:
                    print('Сan\'t divide by zero!')
            except NameError:
                pass

    switch_variable += 1
    
# Вывод результата введенной математической операции:

try:
    if switch_variable <= 2:
        result_massage += str(first_composed_number) + ' ' + operation + ' ' + str(second_composed_number) + ' = ' + str(result_arithmetic_operation)
        print(result_massage)

except NameError:
    print('Error message. There is not a mathematical operation')


""" Задание 2:
В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы, 
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать количество нулей. Результаты 
вывести на экран. """

import random

negative_numbers = 0
positive_numbers = 0
zero_numbers = 0
length_list = int(input('Введите количество целых чисел: '))

spisok_integer = [random.randint(-100,100) for i in range(length_list)]

min_number = min(spisok_integer)
max_number = max(spisok_integer)

for elem in spisok_integer:
    if elem < 0:
        negative_numbers += 1
    elif elem > 0:
        positive_numbers += 1
    elif elem == 0:
        zero_numbers += 1
        
print(f'Рандом: {spisok_integer}\nМакс: {max_number}\nМин: {min_number}\nБольше нуля: {positive_numbers}\nМеньше нуля: {negative_numbers}\nНулей: {zero_numbers}')