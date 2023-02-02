# Модуль 3. Циклы. Часть 4

""" Задание 1
Показать на экран все простые числа в диапазоне, указанном пользователем. Число называется простым, если оно делится без остатка только на 
себя и на единицу. Например, три — это простое число, а четыре нет. """

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

switch_variable = 0

if digit_1 <= digit_2:
    res = f'Простые числа в диапазоне {digit_1}..{digit_2}: '
    switch_variable = 1
else:
    res = f'Простые числа в диапазоне {digit_2}..{digit_1}: '


if switch_variable == 1:
    while digit_1 <= digit_2:
        prime_num = True
        digit = digit_1 if digit_1 >= 0 else -digit_1

        for i in range(2, digit):
            if digit % i == 0:
                prime_num = False
                break
        
        if prime_num == True:
            res += str(digit) + ', ' if digit_1 >=0 else str(-digit) + ', '
        
        digit_1 += 1
else:
    while digit_2 <= digit_1:
        prime_num = True
        digit = digit_2 if digit_2 >= 0 else -digit_2

        for i in range(2, digit):
            if digit % i == 0:
                prime_num = False
                break
        
        if prime_num == True:
            res += str(digit) + ', ' if digit_2 >=0 else str(-digit) + ', '
        
        digit_2 += 1

res = res[:-1]
print(res.rstrip(','), '.', sep= '')

""" Задание 2
Показать на экране таблицу умножения для всех чисел от 1 до 10. Например: 1 * 1 = 1 1 * 2 = 2 ….. 1 * 10 = 10
.........................................................................
10 * 1 = 10 10 * 2 = 20 …. 10 * 10 = 100. """

res = ''

for i in range(1, 11): 
    for j in range(1,11):
        if len(str(i * j)) == 2 and len(str(i)) != 2:
            res += f'{i} * {j} = {i * j}  |'
        elif len(str(i)) == 2 and len(str(i * j)) != 3:
            res += f'{i} * {j} = {i * j} |'
        elif len(str(i * j)) == 3:
            res += f'{i} * {j} = {i * j}|'
        else:
            res += f'{i} * {j} = {i * j}   |'
    res += '\n'

print(res)

""" Задание 3
Показать на экран таблицу умножения в диапазоне, указанном пользователем. Например, если пользователь указал 3 и 5, таблица может выглядеть 
так 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30 
.....................................................................................
5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50 """

while True:
    try:    
        digit_1 = int(input('Enter the first number: '))
        digit_2 = int(input('Enter the second number: '))
        if digit_1 <= 0 or digit_2 <= 0 or digit_1 > 10 or digit_2 > 10:
            raise Exception
        else:
            break
    except ValueError:
        print('ERROR!!!\nYou didn\'t enter a number.\nERROR!!!')
    except Exception:
        print('ERROR!!!\nEnter numbers in the range 1-10\nERROR!!!')

res = ''

if digit_1 <= digit_2:
    for i in range(digit_1, digit_2 + 1): 
        for j in range(1,11):
            if len(str(i * j)) == 2 and len(str(i)) != 2:
                res += f'{i} * {j} = {i * j}  |'
            elif len(str(i)) == 2 and len(str(i * j)) != 3:
                res += f'{i} * {j} = {i * j} |'
            elif len(str(i * j)) == 3:
                res += f'{i} * {j} = {i * j}|'
            else:
                res += f'{i} * {j} = {i * j}   |'
        res += '\n'
else:
    while digit_1 >= digit_2:
        for j in range(1,11):
            if len(str(digit_1 * j)) == 2 and len(str(digit_1)) != 2:
                res += f'{digit_1} * {j} = {digit_1 * j}  |'
            elif len(str(digit_1)) == 2 and len(str(digit_1 * j)) != 3:
                res += f'{digit_1} * {j} = {digit_1 * j} |'
            elif len(str(digit_1 * j)) == 3:
                res += f'{digit_1} * {j} = {digit_1 * j}|'
            else:
                res += f'{digit_1} * {j} = {digit_1 * j}   |'
        digit_1 -= 1
        res += '\n'

print(res)

# Вопрос. Цикл for может только работать на увеличение шага в диапазоне? Чтобы вывести таблицу умножения с, например, 10 до 1 (когда digit_1 > digit_2) пришлось использовать цикл while и в нем уже уменьшать шаг. Пробовал изменить range от большего к меньшему, но шаг был всеравно от меньшего к большему.

# Ответ
#Дмитрий Владимирович, цикл for может двигаться от большего к меньшему, если в функции range() сделать шаг отрицательным. Например, range(10, 1, -1)
# Тогда получим диапазон: [10, 9, 8...2]