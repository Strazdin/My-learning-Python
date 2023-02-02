""" Задание 1
Напишите информационную систему «Сотрудники».
Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
указанного пользователем файла. """

teammate = {'PersonId': '', 'FirstName': '', 'LastName': '', 'PersonAge': ''}

phone = {'PhoneId': '', 'PersonId': '', 'PhoneNumber': ''}

def show_system_menu():
    print('Информационная система "Сотрудники"')

def choose_from_menu():
    return int(input('1 - ввод данных\b2 - редактирование данных\n3 - удаление\n4 - поиск\n5 - сохранить изменения'))

def go_to_action():
    actions = {1: enter_teammate_information(), 2: edit_teammate_data(), 3: remove_teammate(), 4: find_teammate(), 5: save_changes()}
    actions[choose_from_menu]()

def enter_teammate_information():
    pass

def edit_teammate_data():
    pass

def remove_teammate():
    pass

def find_teammate():
    def search_teammate_by_firs_name():
        pass

    def search_teammate_by_last_name():
        pass

    def show_all_teammates_information():
        pass

    def search_teammates_by_specified_letter():
        pass
    pass

def save_changes():
    pass

