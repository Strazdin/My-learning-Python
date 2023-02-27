#Задание 1.

class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, phone_number) -> None:
        if name not in self.phonebook.keys():
            self.phonebook[name] = phone_number
            print(f'{name} - {phone_number} успешно добавлен!')
        else:
            print('Сообщение об ошибке')

    def remove_contact(self, name) -> None:
        if name in self.phonebook.keys():
            del self.phonebook[name]
            print(f'контакт успешно удален!')
        else:
            print('Сообщение об ошибке')

    def update_contact(self, name, phone_number) -> None:
        if name in self.phonebook.keys():
            self.phonebook[name] = phone_number
        else:
            print('Сообщение об ошибке')
    
    def get_contact(self, name) -> str:
        return self.phonebook[name]
    
    def get_all_contacts(self) -> list:
        lst_phonebook = []

        for key, value in self.phonebook.items():
            lst_phonebook.append([key, value])

        return lst_phonebook

phonebook = Phonebook()
phonebook.add_contact('name1', '+111111111')
phonebook.add_contact('name2', '+211111111')
phonebook.add_contact('name1', '+111111111')
phonebook.update_contact('name122', '+12345678')
phonebook.update_contact('name1', '+12345678')
print(phonebook.get_all_contacts())
print(phonebook.get_contact('name1'))
phonebook.remove_contact('name1')
print(phonebook.get_all_contacts())

#Задание 2.
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.time = 0

    def format_time(self, time):
        return round(time, 3)
    
    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            print('Таймер уже запущен')

    def stop(self):
        if self.start_time is not None:
            self.time = self.format_time(time.time() - self.start_time)
        else:
            print('Таймер не был запущен')

    def reset(self):
        self.start_time = None

    def elapsed_time(self):
        if self.start_time:
            return self.format_time(time.time() - self.start_time)
        return 'Таймер не был запущен'
    
timer = Timer()
timer.start()
[i for i in range(9999999)]
timer.stop()
print(timer.time)
[i for i in range(9999999)]
print(timer.elapsed_time())
timer.reset()