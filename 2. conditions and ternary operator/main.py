""" Задание 1
Пользователь вводит с клавиатуры номер дня недели 
(1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник, 
2 — вторник и т.д.  """

num_day_of_week = int(input('Enter the number of the day of the week\n(1-7): '))

if num_day_of_week == 1:
    print('Monday')
elif num_day_of_week == 2:
    print('Tuesday')
elif num_day_of_week == 3:
    print('Wednesday')
elif num_day_of_week == 4:
    print('Thursday')
elif num_day_of_week == 5:
    print('Friday')
elif num_day_of_week == 6:
    print('Saturday')
elif num_day_of_week == 7:
    print('Sunday')
else:
    print('Error message')


""" Задание 2
Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на экран название месяца. 
Например, если 1, то на экране надпись январь, 2 — февраль и т.д.  """



""" Задание 3
Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись «Number is positive», 
если меньше нуля «Number is negative», если равно нулю «Number is equal to zero» """

digit = int(input('Enter any number: '))

if digit > 0:
    print('Number is positive')
elif digit < 0:
    print('«Number is negative')
else:
    print('Number is equal to zero')

""" Задание 4
Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке 
возрастания."""

digit1 = int(input('Enter the 1st digit: '))
digit2 = int(input('Enter the 2nd digit: '))

if digit1 == digit2:
    print(f'Number {digit1} is equal to number {digit2}')
else:
    if digit1 > digit2:
        print(f'{digit2}, {digit1}')
    else:
        print(f'{digit1}, {digit2}')
