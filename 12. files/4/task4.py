""" Задание 4
Дан текстовый файл. Найти длину самой длинной 
строки. """

text = []

with open('text1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        text.append(len(line.rstrip()))
        
print('Длина самой длинной строки: ')
print(max(text))
print('Максимальная строка по счету: ')
print(text.index(max(text)) + 1)