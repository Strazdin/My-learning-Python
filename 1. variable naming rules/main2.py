""" Задание 1 
Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры. Например, если с клавиатуры введено 1, 5, 7, 
тогда нужно сформировать число 157. """

digit1 = input('Enter the 1st digit digit: ')
digit2 = input('Enter the 2nd second digit: ')
digit3 = input('Enter the 3rd third digit: ')
result = digit1 + digit2 + digit3
result = int(result)
print(f'You entered numbers: {digit1}, {digit2}, {digit3}\nResult: {result}')


""" Задание 2
Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр. Например, если с клавиатуры введено 
1324, тогда результат произведения 1*3*2*4 = 24. """


digit = int(input('Enter a four digit number: '))
digit1, digit = digit % 10, digit // 10
digit2, digit = digit % 10, digit // 10
digit3, digit = digit % 10, digit // 10
digit4, digit = digit % 10, digit // 10 
result_multiplication = digit1 * digit2 * digit3 * digit4
print(f'Result:\n{digit4} * {digit3} * {digit2} * {digit1} = {result_multiplication}')

""" Задание 3
Пользователь вводит с клавиатуры количество метров. Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили."""

meters = int(input('Enter the number of meters: '))
centimeters = meters * 0.01
decimeters = meters * 0.1
millimeters = meters * 0.001
miles = meters *  0.000621
print(f'Result: {meters} meters = {centimeters} centimeters\n{meters} meters = {decimeters} decimeters\n{meters} meters = {millimeters} millimeters\n{meters} meters = {miles} miles\n')
# Вопрос: не получается представить print в читаемом виде... Ставлю пробел вроде как ошибка становится...

""" Задание 4
Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер основания треугольника и размер высоты. """

base_triangle = int(input('Enter a base of a triangle: '))
height_triangle = int(input('Enter a height of a triangle: '))
triangle_area = 0.5 * base_triangle * height_triangle
print(f'The area of the triangle is {triangle_area}')

""" Задание 5
Пользователь с клавиатуры вводит четырёхзначное число. Необходимо перевернуть число и отобразить  """

digit = int(input('Enter a four digit number: '))
digit1, digit = digit % 10, digit // 10
digit2, digit = digit % 10, digit // 10
digit3, digit = digit % 10, digit // 10
digit4, digit = digit % 10, digit // 10 
print(f'Result:\n{digit1}{digit2}{digit3}{digit4}')
