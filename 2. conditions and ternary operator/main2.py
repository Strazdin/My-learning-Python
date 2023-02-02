""" Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. 
Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно 
вывести само число. Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке. """

digit = int(input('Enter a number in the range 1-100: '))
number_devide_3 = digit % 3
number_devide_5 = digit % 5

if not digit > 100 or digit < 1:
    if number_devide_3 == 0 and number_devide_5 == 0:
        print('Fizz Buzz')
    elif number_devide_5 == 0:
        print('Buzz')
    elif number_devide_3 == 0:
        print('Fizz')
    else:
        print(f'{digit}')
else:
    print('Error message')


""" Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой до седьмой включительно. """

digit = int(input('Enter a number: '))
power = int(input('Enter power of the number\n(0-7): '))
i = 0

# Немного не понял условие задачи, сделал два варианта:

while i <= 7:
    print(digit ** i)
    i += 1

print('\n')

if power == 0:
    print(digit ** 0)
elif power == 1:
    print(digit ** 1)
elif power == 2:
    print(digit ** 2)
elif power == 3:
    print(digit ** 3)
elif power == 4:
    print(digit ** 4)
elif power == 5:
    print(digit ** 5)
elif power == 6:
    print(digit ** 6)
elif power == 7:
    print(digit ** 7)
else:
    print('Error message')

""" Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит стоимость разговора и выбирает с какого 
на какой оператор он звонит. Вывести стоимость на экран.
"""

operator = (input('Select operator\nEnter MTC or Tele2 or Beeline: '))
dutation_of_call = int(input('Enter the duration of the call (minutes): '))
cost_of_call = 0
operator_cost_1 = 1
operator_cost_2 = 1.5
operator_cost_3 = 2

if operator == 'MTC':
    cost_of_call = dutation_of_call * operator_cost_1
elif operator == 'Tele2':
    cost_of_call = dutation_of_call * operator_cost_2
elif operator == 'Beeline':
    cost_of_call = dutation_of_call * operator_cost_3
else:
    print('Error message')

print(f'Call cost is {cost_of_call}(currency)')

""" Задание 4
Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%. Пользователь вводит с 
клавиатуры уровень продаж для трех менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию 200$, вывести 
итоги на экран. """

result = 'Result:\n'
i = 1
salary = 0
manager_number = 0

while i <= 3:
    sales_level_for_manager = int(input(f'Enter the sales level for manager {i}: '))

    if sales_level_for_manager > salary:
        salary = sales_level_for_manager
        manager_number = i

    if sales_level_for_manager < 500:
        result += f'Manager\'s salary {i}: {200 + sales_level_for_manager * 0.03}\n'
    elif sales_level_for_manager <= 1000:
        result += f'Manager\'s salary {i}: {200 + sales_level_for_manager * 0.05}\n'
    elif sales_level_for_manager > 1000:
        result += f'Manager\'s salary {i}: {200 + sales_level_for_manager * 0.08}\n'
    
    i += 1

result += f'\nThe best manager is manager {manager_number}\nHe will receive a bonus salary + 200$\n'
print('\n')
print(result)