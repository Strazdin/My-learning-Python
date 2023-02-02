""" Задание 1
Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y. """

x = int(input('Enter a number: '))
y = int(input('Enter the degree of the number: '))
res = 1
number = x
degree = y

if y == 0:
    x = 1
elif y == 1:
    res = x
else:
    while y > 0:
        res *= x
        y -= 1

print(f'{number}^{degree}={res}')

""" Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры. """

i= 100
counter = 0

while i >= 100 and i <= 999:
    digit = i
    digit1, digit = digit % 10, digit // 10
    digit2, digit = digit % 10, digit // 10
    digit3, digit = digit % 10, digit // 10

    if digit1 == digit3 or digit1 == digit2 or digit3 == digit2:
        counter += 1
    i += 1

print(counter)



""" Задание 3
Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные. """

i= 100
counter1 = 0
counter2 = 0

while i >= 100 and i <= 9999:
    digit = i
    digit1, digit = digit % 10, digit // 10
    digit2, digit = digit % 10, digit // 10
    digit3, digit = digit % 10, digit // 10
    digit4, digit = digit % 10, digit // 10 
    if i <= 1000:
        if digit2 == digit3 or digit2 == digit4 or digit3 == digit4:
            counter1 += 1
    else:
        if digit1 != digit2 or digit1 != digit3 or digit1 == digit4 or digit2 == digit3 or digit2 == digit4 or digit3 == digit4:
            counter2 += 1
    i += 1

print(counter1 + counter2)

# К сожалению, здесь ^ результат работы неверный

""" Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран. """

num = input('Enter a number: ')
i = 0
res = ''

while i < len(num):
    part_digit = num[i]
    if part_digit != '3' and part_digit != '6':
        res += part_digit
    i += 1

res = 'All digits deleted' if res == '' else res
print(res)