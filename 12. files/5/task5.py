""" Задание 5
Дан текстовый файл. Посчитать сколько раз в нем 
встречается заданное пользователем слово. """
text = ''
word = input('Введите слово, которое нужно посчитать: ')
with open('text1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        text += line.rstrip()

print(text.count(word))