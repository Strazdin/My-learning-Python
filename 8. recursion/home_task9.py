""" Модуль 5. Функции. 
Тема: Функции. Часть 3 """

""" Задание 1
Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел. """

def greatest_divisor(x, y): 
    if y == 0:  
        return x 
    else: 
        return greatest_divisor(y, x % y)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = greatest_divisor(x, y)
print(result)

""" Задание 2
Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен 
угадать его. После ввода пользователем числа программа 
сообщает, сколько цифр числа угадано (быки) и сколько 
цифр угадано и стоит на нужном месте (коровы). После 
отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. В программе 
необходимо использовать рекурсию. """

import random
# Пытался заморочиться с 'интерфейсом'
""" game_hum_or_computer = True #Если True - игра "против компьютера", False - пользователь сам вводит число
flag_choose_setting = True
flag_enter_number = True
x_random = random.randint(1000,9999)


def choose_setting():
    select_game_mode = input('Желаете сыграть с компьютером(Y) или с человеком(N)?\nВедите Y или N: ').strip().capitalize()
    flag_choose_setting = False
    if select_game_mode == 'N':
        game_hum_or_computer == False

def enter_number():
    x_guess = list(input('Угадайте число от 1000 до 9999: '))
    
    if len(str(x_guess)) != len(str(x_random)):
        print("Число должно быть четырехзначным!")
        x_guess = 'ERROR'
        return x_guess
    
    flag_enter_number = False
    return x_guess


def play_bulls_and_cows_game():
    if flag_choose_setting:
        choose_setting()

    if flag_enter_number:
        enter_number()

    if game_hum_or_computer:
        bulls = 0
        cows = 0 """

# В итоге решил сделать просто логику, надеюсь игру правильно понял: 

x_random = [str(random.randint(1, 9)) for i in range(4)]

popytka = 0
bulls = 0 
cows = 0

print(f'Рандом: {x_random}')

def play_bulls_and_cows_game(cows, bulls, count = 4):
    if count == 0:
        print(f'Коров {cows}, быков {bulls}')
        return cows
    
    if x_random[count - 1] == x_guess[count - 1]:
        cows += 1
    
    for i in x_random:
        if i == x_guess[count - 1]:
            bulls += 1

    count -= 1
    play_bulls_and_cows_game(cows, bulls, count)

while True:
    x_guess = list(input('Угадайте число от 1000 до 9999: '))
    print(f'Вы ввели: {x_guess}')

    play_bulls_and_cows_game(cows, bulls)
    popytka += 1

    next_or_stop = input('Желаете продолжить?')

    if next_or_stop == 'N':
        break

print(f'Количество попыток: {popytka}')

