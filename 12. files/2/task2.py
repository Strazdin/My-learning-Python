""" Задание 2
Дан текстовый файл. Необходимо создать новый файл 
и записать в него следующую статистику по исходному 
файлу:
■ Количество символов;
■ Количество строк;
■ Количество гласных букв;
■ Количество согласных букв;
■ Количество цифр. """
count_line = 0
count_vowel = 0
count_consonant = 0 
count_int = 0
text = ''

with open('text1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        count_line += 1
        text += line.rstrip()

print(f'Количество строк = {count_line}')
print(f'Количество символов = {len(text)}')

def is_vowel_letter(letter):
    list_letter_vowel = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']

    if letter in list_letter_vowel:
        return 1
    else:
        return 0

def is_consonant_letter(letter):
    list_letter_consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

    if letter in list_letter_consonant:
        return 1
    else:
        return 0
    
for letter in text:
    if letter.isdigit():
        count_int += 1
    else:
        count_vowel += is_vowel_letter(letter)
        count_consonant += is_consonant_letter(letter)

print(f'Количество цифр = {count_int}')
print(f'Количество гласный = {count_vowel}')
print(f'Количество согласных = {count_consonant}')

with open(file='info_text1.txt', mode='w', encoding='UTF-8') as f:
    f.write(f'Количество строк = {count_line}\nКоличество символов = {len(text)}\nКоличество цифр = {count_int}\nКоличество гласный = {count_vowel}\nКоличество согласных = {count_consonant}')