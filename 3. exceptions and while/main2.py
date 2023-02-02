

""" Задание 1
Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел, 
кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы. """

while True:
    try:    
        digit_1 = int(input('Enter the first number: '))
        digit_2 = int(input('Enter the second number: '))
        if digit_1 == digit_2:
            raise Exception
        else:
            break
    except ValueError:
        print('ERROR!!!\nYou didn\'t enter a number.\nERROR!!!')
    except Exception:
        print('ERROR!!!\nYou entered two of the same number. Enter numbers to make up a range.\nERROR!!!')

sum_even = 0
sum_odd = 0
sum_multiple_of_9 = 0
even_number_counter = 0
odd_number_counter = 0
multiple_of_9_number_counter = 0
switch_variable = 0
arithmetic_mean_even = 0
arithmetic_mean_odd = 0
arithmetic_mean_multiple_of_9 = 0

if digit_1 <= digit_2:
    switch_variable = 1

if switch_variable == 1:
    while digit_1 <= digit_2:
        digit = digit_1 if digit_1 >= 0 else -digit_1

        if digit_1 % 2 == 0 and digit_1 != 0:
            sum_even += digit
            even_number_counter += 1
        else:
            if digit_1 % 9 != 0:
                sum_odd += digit
                odd_number_counter += 1
            else:
                if digit_1 != 0:
                    sum_multiple_of_9 += digit
                    multiple_of_9_number_counter += 1

        print(digit_1)
        digit_1 += 1
else:
    while digit_2 <= digit_1:
        digit = digit_2 if digit_2 >= 0 else -digit_2

        if digit_2 % 2 == 0 and digit_2 != 0:
            sum_even += digit
            even_number_counter += 1
        else:
            if digit_2 % 9 != 0:
                sum_odd += digit
                odd_number_counter += 1
            else:
                if digit_2 != 0:
                    sum_multiple_of_9 += digit
                    multiple_of_9_number_counter += 1

        print(digit_2)
        digit_2 += 1

sum_even = sum_even if sum_even >= 0 else -sum_even 
sum_odd = sum_odd if sum_odd >= 0 else -sum_odd 
sum_multiple_of_9 = sum_multiple_of_9 if sum_multiple_of_9 >= 0 else -sum_multiple_of_9

arithmetic_mean_even = 0 if even_number_counter == 0 else sum_even // even_number_counter
arithmetic_mean_odd = 0 if odd_number_counter == 0 else sum_odd // odd_number_counter
arithmetic_mean_multiple_of_9 = 0 if multiple_of_9_number_counter == 0 else sum_multiple_of_9 // multiple_of_9_number_counter

print(f'The sum of the even numbers: {sum_even}. The arithmetic mean of these numbers is {arithmetic_mean_even}\nThe sum of the odd numbers: {sum_odd}. The arithmetic mean of these numbers is {arithmetic_mean_odd}\nThe sum of the multiple of 9 numbers: {sum_multiple_of_9}. The arithmetic mean of these numbers is {arithmetic_mean_multiple_of_9}\n')

# Мой комментарий: идея была реализовать программу, которая работает как с отрицательным диапазоном, так и с положительным, а также 
# автоматически определяла нижнюю и верхнюю границу диапазона.

# столкнулся с проблемой при тестировании, когда допустим нет чисел кратных 9, программа выходит с ошибкой "ZeroDivisionError", так как 
# счетчик этих чисел изначально равен 0. Пришлось решать эту проблему через тернарные операторы.
# А также пришлось так скажем "загромождать" программу теми же тернарниками, чтобы реализовать работу с отрицательными числами диапазона 
# (отрицательные числа превращать в положительные) 

# Вопрос: как бы Вы тут сделали такой функционал, который был написан в "мой комментарий"? Ну, с делением на ноль, наверное, можно было где-нибудь исключение поставить... а с отрицательными числами может есть какая-то функция-метод для этого дела...
# Честно говоря, решая эту задачу вы проделали огромную работу, поэтому как-то не хочется всё это менять на другой, свой вариант. Что касается отрицательных чисел, то да, действительно можно было бы что-то сделать с добавлением более сложных функций.
# Но не переживайте, всему своё время)

""" Задание 2
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. Нужно отобразить на экране вертикальную линию из введенного 
символа, указанной длины. 
Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
    %
    %
    %
    %
    % """

""" line_length = int(input('Enter a line length: '))
symbol= input('Enter a symbol: ')
i = 0

while i < line_length:
    print('\t' + symbol)
    i += 1 """

"""  Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive», если меньше нуля «Number is 
negative», если равно нулю «Number is equal to zero». Когда пользователь вводит число 7 программа прекращает свою работу и выводит 
на экран надпись «Good bye!» """

""" while True:
    digit = int(input('Enter a digit: '))
    if digit != 7:
        if digit > 0:
            print('Number is positive')
        elif digit < 0:
            print('«Number is negative')
        else:
            print('Number is equal to zero')
    else:
        break

print('Good bye!')
 """
""" Задание 4
Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. Когда пользователь вводит 
число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»"""

digit_min = 0
digit_max = 0
sum = 0
entered_numbers = ''

while True: 

    digit = int(input('Enter a digit: '))
    
    if digit == 7:
        print('Good bye!')
        break
    elif digit > digit_max:
        digit_max = digit
    elif digit < digit_min:
        digit_min = digit
    sum += digit
    entered_numbers += str(digit) + ' '

print(f'Max: {digit_max};\nMin: {digit_min};\nSum: {sum}\nEntered numbers: {entered_numbers}')
