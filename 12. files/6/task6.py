""" Задание 6
Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется 
пользователем. """

text = ''
word = input('Введите слово, которое нужно найти: ')
new_word = input('Введите слово, которое нужно заменить: ')
with open('text.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        text += line.rstrip()

text_list = text.split()

count = 0
if word in text_list:
    for i, item in enumerate(text_list):
        if text_list[i] == word:
            text_list[i] = new_word
            count += 1
    print(f'слово "{word}" заменили в количестве - {count}')
else:
    print(f'Слова {word} нет в файле')

with open(file='info_text1.txt', mode='w', encoding='UTF-8') as f:
    f.write(' '.join(text_list))