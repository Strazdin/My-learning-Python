""" Модуль 5. Функции.
Тема: Функции. Часть 1 """

""" Задание 1
Напишите функцию, которая отображает на экранформатированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates """

def show_text():
    return print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\n\n\t\t\t\t\tBill Gates")

show_text()

print('\n')
""" Задание 2
Напишите функцию, которая принимает два числав качестве параметра и отображает все четные числа
между ними. """

def show_even_numbers_in_range(num1: int, num2: int):
    if num1 <= num2:
        while num1 <= num2:
            if num1 % 2 == 0:
                print(num1)
            
            num1 += 1
    else:
        while num2 <= num1:
            if num2 % 2 == 0:
                print(num2)
            
            num2 += 1

show_even_numbers_in_range(10, 1)

print('\n')
""" Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой. """

def show_square(lenght_side: int, symbol: str, logic = True):
    line = lenght_side * symbol

    if logic:
        for _ in range(lenght_side):
            print(line)
    else:
        print(line)
        for _ in range(lenght_side - 2):
            print(symbol + " " * (lenght_side - 2) + symbol)
        print(line)    
        
        
show_square(8, "#", False)
print('\n')
show_square(symbol = "#", lenght_side = 8)

print('\n')
""" Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров. """

import random
list_numbers = [random.randint(6, 18) for i in range(random.randint(4,5))]
print(list_numbers)

def is_five_numbers(number_list: list):
    return len(number_list) == 5
    
def get_min_beetwen_five_numbers(number_list: list):
    if is_five_numbers(number_list):
        return min(number_list)
    else:
        return 'ERROR MESAGE'

result = get_min_beetwen_five_numbers(list_numbers)
print(result)

print('\n')
# /Немного не понял точно как надо сделать, поэтому напишу второй вариант и вопрос связанный с ним:

def get_min(num1, num2, num3, num4, num5):
    list_num = []
    list_num.append(num1)
    list_num.append(num2)
    list_num.append(num3)
    list_num.append(num4)
    list_num.append(num5)
    # Можно ли чтобы не писать много раз append сделать что-то вроде этого?
            # ДА, можно просто сразу записать list_num = [num1,num2,num3,num4,num5]
    # for i in range(5):
        # list_num.append(f'num{i + 1}')
    return min(list_num)

result = get_min(5,2,7,5,8)
print(result)

print('\n')
""" Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами. """

def multiplication_numbers_in_range(lower_value: int, upper_value: int):
    if lower_value <= upper_value:
        result = lower_value
        while lower_value < upper_value:
            lower_value += 1
            result *= lower_value                     
    else:
        result = upper_value
        while upper_value < lower_value:
            upper_value += 1
            result *= upper_value

    return result
            
result = multiplication_numbers_in_range(5, 1)
print(result)

print('\n')
""" Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4. """

def get_amount_digits_in_number(number: int):
    return len(str(number))

print(get_amount_digits_in_number(1234567))

print('\n')
""" Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром.  """

def get_palindrom(number: int):
    return str(number) == str(number)[::-1]

print(get_palindrom(12321))