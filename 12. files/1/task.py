""" Задание 1
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла. """

with open('text1.txt', 'r', encoding='UTF-8') as file:
    with open('text2.txt', 'r', encoding='UTF-8') as file2:
        for f, b in zip(file, file2):
            if f != b:
                print(f[:-1])
                print(b[:-1])
