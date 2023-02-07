""" Задание 3
Дан текстовый файл. Удалить из него последнюю 
строку. Результат записать в другой файл. """
text = ''
with open('text1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        text = line.rstrip()

with open(file='info_text1.txt', mode='w', encoding='UTF-8') as f:
    f.write(text)