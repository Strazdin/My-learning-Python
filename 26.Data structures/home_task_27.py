# Задание 1.

class WordCounter:
    def __init__(self):
        self.words = {}

    def read_file(self, file_name):
        with open(f'{file_name}', 'r', encoding='utf-8') as f:
            import re
            words = re.split(r'[\-,.:;\s]+', f.read())
            for word in words:
                if word in self.words:
                    self.words[word] += 1
                else:
                    self.words[word] = 1

    def head(self):
        frequent_word = []

        for keys, values in self.words.items():
            frequent_word .append((values,keys))

        frequent_word.sort(reverse = True)

        for key, val in frequent_word[:10]:
            print (f'Частота - {key}, Слово - {val}')



reader = WordCounter()
reader.read_file('text.txt')
reader.head()


2.
import json
import csv


class CsvToJson:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def convert(self, json_file_path):
        data = {}
        with open(self.csv_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                for key, value in row.items():
                    if key not in data:
                        data[key] = []
                    data[key].append(value)
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)


converter = CsvToJson('file.csv')
converter.convert('file2.json')


3.
import os

class RenameFile:
    def __init__(self):
        self.history = {}

    def rename(self, file, new_name):
        self.history[file] = new_name
        os.replace(file, new_name)


a = RenameFile()
a.rename('file.csv', 'table.csv')
a.rename('text.txt', 'file.txt')
print(a.history)