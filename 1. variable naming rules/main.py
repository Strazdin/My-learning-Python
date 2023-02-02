""" Задание 1
Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат 
вычислений вывести на экран. """

digit1 = int(input('Enter the 1st digit: '))
digit2 = int(input('Enter the 2nd digit: '))
digit3 = int(input('Enter the 3rd digit: '))
result_sum = digit1 + digit2 + digit3
result_multiplication = digit1 * digit2 * digit3
print(f'The result of the sum of the numbers: {result_sum}.\nThe result of the multiplication of the numbers: {result_multiplication}')
# Вопрос: в каких случаях нужно оставлять пустые строки, т.е между какими конструкциями для улучшения читаемости кода? Понимаю, еще мало изучили их, ну вот, например, здесь, выше и далее, хотелось бы понять. 

""" Задание 2
Пользователь вводит с клавиатуры три числа. Первое 
число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность за коммунальные услуги.
Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат. """

salary = int(input('Enter your salary for the month: '))
credit = int(input('Enter the amount of the credit: '))
taxes = int(input('Enter the debt your utilities: '))
amount_after_payments = salary - credit - taxes
print(f'You\'ll get {amount_after_payments}(currency) after all payments')
# Вопрос: наименование переменных из двух и более слов идет с учетом артиклей или предлогов? Просто заметил Вы на уроке писали два слова а между ними of. Хотел бы уточнить этот вопрос.

""" Задание 3
Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей. """

diagonal_1 = int(input('Enter the length of the 1st diagonal: '))
diagonal_2 = int(input('Enter the length of the 2nd diagonal: '))
rhombus_area =  (diagonal_1 + diagonal_2) / 2
print(f'The area of a rhombus is equal {rhombus_area}(unit)')
# Вопрос: буква "l" очень похожа на "1", числа тоже можно разделять в таких случаях нижним подчеркиванием?

""" Задание 4
Выведите на экран надпись To be or not to be на разных строках. Пример вывода:
To be 
or not
to be """

print("""To be
or not
to be
""")

""" Задание 5
Выведите на экран надпись «Life is what happens when you're busy making other plans» John Lennon на разных 
строках. Пример вывода:
“Life is what happens
 when
 you're busy making other plans”
 John Lennon """

print('Life is what happens\nwhen\nyou\'re busy making other\nplans\nJohn Lennon')