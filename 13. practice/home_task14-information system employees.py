""" Задание 1
Напишите информационную систему «Сотрудники».
Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
указанного пользователем файла. """

# Отличия от задания: пользователь не указывает имя файла из которого будет происходить выгрузка.
# Вместо этого загружается два файла, если они существуют, если нет, то создаются
# Эти два файла хранят информацию, один файл о командах, второй о их тиммейтах
# Основная идея была поработать с подобиями БД с двумя таблицами, которые имеют общий id (не помню какая тут связь сделана)
# По задаче: сделал много строк кода из-за метода решения "влоб", наверняка можно сократить строчки кода, улучшив структуру, но цель была именно в практике (встречается много повторяемого кода)
# хотелось, конечно, сделать код не повторяемый, но с ходу спроектировать полную структуру программы пока еще не получается, чтобы не переписывать код

def get_dictionary_file(file_name) -> dict:
    def create_dictionary(file_name):
        teammate = {'PersonId': [], 'TeamId': [], 'FirstName': [], 'LastName': [], 'PersonAge': []}
        teamName = {'TeamId': [], 'TeamName': [], 'Country': []}

        dict_names = {'teammate': teammate, 'teamName': teamName}
        with open(f'{file_name}.json', "w") as file:
            json.dump(dict_names[file_name], file)
    
    import json
    import os.path

    if not os.path.isfile(f'./{file_name}.json'):
        create_dictionary(file_name)

    dictionary = {}

    with open(f'{file_name}.json', encoding='UTF-8') as file:
        dictionary = json.load(file)

    return dictionary

def go_to_action():
    error_variable = 0
    next_or_exit = 0
    actions_teammate = {'1': enter_teammate_information, '2': edit_teammate_data, '3': remove_teammate, '4': find_teammate, '5': save_changes}
    actions_teamName = {'1': add_team}

    teammates = get_dictionary_file('teammate')
    teams = get_dictionary_file('teamName')

    while error_variable <= 3:
        print(teammates)
        print(teams)
        print('\nДобро пожаловать в навигационную систему "Teammates"')
        if len(teams['TeamId']) == 0:
            choice_message = input('\nВнимание! В базе данных нет никакой команды, желаете добавить команду?\nВведите:\n1 - значит "да"\nлюбой другой символ - выход из системы\n: ').strip()
            if choice_message == '1':
                actions_teamName['1'](teams)
                error_variable += 1
                continue
            else:
                break
        else:
            print('В базе хранятся команды: ')

            for column, line in teams.items():
                if column == 'TeamName':
                    teams_name = line
                elif column == 'Country':
                    teams_countries = line

            for name, country in zip(teams_name, teams_countries):
                print(f'"{name}" из страны: {country}')
            
            if next_or_exit == 0:
                choice_message_team = input('Введите команду с которой будете проводить действия: ').strip().capitalize()
                next_or_exit = 1
            else:
                choice = input(f'Желаете продолжить работу с командой {choice_message_team} или выйти в главное меню?\nВведите:\n1 - значит "да"\nлюбой другой символ - выход в главное меню\n: ').strip()
                if choice == '1':
                    pass
                else:
                    next_or_exit = 0
                    continue

            if choice_message_team in teams['TeamName']:
                teams_id = teams_name.index(choice_message_team) + 1
            else:
                print(f'команда {choice_message_team} не найдена!')
                error_variable += 1
                next_or_exit = 0
                continue
        
        navigation = input("""Введите цифру, чтобы сделать:
            1 - ввод данных
            2 - редактирование данных
            3 - удаление
            4 - поиск
            5 - сохранить изменения
            : """).strip()

        if navigation in actions_teammate:
            if navigation == '4' or  navigation == '5' or  navigation == '2' or  navigation == '3':
                actions_teammate[navigation](teammates, teams)
            else:
                actions_teammate[navigation](teammates, teams_id)

        elif navigation == 'exit' or navigation == 'e':
            print('Message: До скокрой встречи!')

            save_changes(teammates, teams)
            break
        else:
            error_variable += 1

            if error_variable != 4:
                print('Message: ошибка ввода')
            else:
                print('Message: обнаружены подозрительные попытки ввода. Программа вынуждена закрыться')

            print("\n")
# 
def is_int(age):
    try:
        print(int(age))
        int(age)
        return True
    except ValueError:
        return False
    
def is_working_age(age):
    return int(age) >= 14 and int(age) <= 50

def is_valid_initials(initials, length = 0):
    def word_length_is_greater_than(initials, length):
        return len(initials) >= length

    letters_filter = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"," ","-","_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for one_char in initials.lower():
        if one_char not in letters_filter:
            return False
        
    if length != 0:
        return word_length_is_greater_than(initials, length)

    return True
# 
def add_team(team):
    print('---Добавить команду---')

    prompt = ''

    while True:
        team_name = input(f'Введите имя команды{prompt}: ').strip().capitalize()

        if team_name == '':
            break

        team_country = input(f'С какой страны команда "{team_name}"?\n: ').strip().capitalize()
        prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'

        if is_valid_initials(team_name) and is_valid_initials(team_country, length_last := 2):
            for column, line in team.items():
                if column == 'TeamId':
                    team[column].append(int(line[-1]) + 1) if len(line) != 0 else team[column].append(1)
                elif column == 'TeamName':
                    team[column].append(team_name)
                elif column == 'Country':
                    team[column].append(team_country)

            print(f'\nMessage: команда "{team_name}" - {team_country} успешно добавлена!\n')
        else:
            print('Message: Сообщение об ошибке')
            break

def enter_teammate_information(teammate, teams_id):    
    prompt = ''

    while True:
        print('---Добавить в команду---')
        first_name = input(f'Введите имя члена команды{prompt}: ').strip().capitalize()

        if first_name == '':
            break

        last_name = input('Введите фамилию члена команды: ').strip().capitalize()       
        person_age = input('Введите возраст члена команды: ').strip()
        prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'
        if is_valid_initials(first_name, length_first := 3) and is_valid_initials(last_name, length_last := 2) and is_int(person_age) and is_working_age(person_age):
            for column, line in teammate.items():
                if column == 'PersonId':
                    teammate[column].append(int(line[-1]) + 1) if len(line) != 0 else teammate[column].append(1)
                elif column == 'TeamId':
                    teammate[column].append(teams_id)
                elif column == 'FirstName':
                    teammate[column].append(first_name)
                elif column == 'LastName':
                    teammate[column].append(last_name)
                elif column == 'PersonAge':
                    teammate[column].append(person_age)

            print(f'\nMessage: {first_name} {last_name} успешно добавлен в команду!\n')
        else:
            print('Message: Сообщение об ошибке')
            break

        # print(teammate)
        

def edit_teammate_data(teammate, teams):
    print('---Редактирование данных тиммейта---')

    def edit_first_name(teammate, id):
        print('---Редактирование имени---')
        error = 0

        while True:
            new_first_name = input('Введите новое имя: ').strip().capitalize()

            if is_valid_initials(new_first_name, length_first := 3):
                teammate['FirstName'][id - 1] = new_first_name
                print('Имя успешно изменено!\n')
                break
            else:
                print(f'Message: Сообщение об ошибке. Имя "{new_first_name}" не допустимое!')
                error += 1

                if error >= 3:
                    print('message: слишком частые попытки неправильного ввода!')
                    break


    def edit_last_name(teammate, id):
        print('---Редактирование фамилии---')
        error = 0

        while True:
            new_last_name = input('Введите новую фамилию: ').strip().capitalize()

            if is_valid_initials(new_last_name, length_first := 2):
                teammate['LastName'][id - 1] = new_last_name
                print('Фамилия успешно заменена!\n')
                break
            else:
                print(f'Message: Сообщение об ошибке. Фамилия "{new_last_name}" не допустима!')
                error += 1

                if error >= 3:
                    print('message: слишком частые попытки неправильного ввода!')
                    break

    def edit_age(teammate, id):
        print('---Редактирование возраста---')
        error = 0

        while True:
            new_age = input('Введите новый возраст: ')

            if is_int(new_age) and is_working_age(new_age):
                teammate['PersonAge'][id - 1] = new_age
                print('Возраст успешно изменен!\n')
                break
            else:
                print(f'Message: Сообщение об ошибке. Возраст "{new_age}" не допустим!')
                error += 1

                if error >= 3:
                    print('message: слишком частые попытки неправильного ввода!')
                    break

    for ind_id in range(len(teammate["PersonId"])):
        first_name = teammate['FirstName'][ind_id]
        last_name = teammate['LastName'][ind_id]
        age = teammate['PersonAge'][ind_id]
        team_id = teammate['TeamId'][ind_id]

        for ind in range(len(teams['TeamId'])):
            if teams['TeamId'][ind] == team_id:
                team_name = teams['TeamName'][ind]

        print(f'Id - {ind_id + 1}. Имя - {first_name}, Фамилия - {last_name}, Возраст - {age}, команда - {team_name}')

    prompt = ''
    error = 0

    while True:
        try:
            id = int(input(f'Введите номер id для редактирования{prompt}: ').strip())
        except ValueError:
            break

        prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'

        if id in teammate["PersonId"]:
            first_name = teammate['FirstName'][id - 1]
            last_name = teammate['LastName'][id - 1]
            age = teammate['PersonAge'][id - 1]
            print(f'По указанному id "{id}" есть тиммейт:')
            print(f'Имя - {first_name}, Фамилия - {last_name}, Возраст - {age}')
            navigation = input("""Что именно редактировать у тиммейта? Введите цифру:
            1 - имя
            2 - фамилия
            3 - возраст
            или любой символ, чтобы вернуться в главное меню
            : """).strip()
            actions = {'1': edit_first_name, '2': edit_last_name, '3': edit_age}

            if navigation in actions:
                actions[navigation](teammate, id)
            else:
                break
        else:
            print(f'message: id номер {id} не существует!')
            error += 1
            if error >= 3:
                print('message: слишком частые попытки неправильного ввода!')
                break



def remove_teammate(teammate, teams):
    prompt = ''
    error = 0

    while True:
        print('---Удаление тиммейта---')

        for ind_id in range(len(teammate["PersonId"])):
            first_name = teammate['FirstName'][ind_id]
            last_name = teammate['LastName'][ind_id]
            age = teammate['PersonAge'][ind_id]
            team_id = teammate['TeamId'][ind_id]

            for ind in range(len(teams['TeamId'])):
                if teams['TeamId'][ind] == team_id:
                    team_name = teams['TeamName'][ind]

            print(f'Id - {ind_id + 1}. Имя - {first_name}, Фамилия - {last_name}, Возраст - {age}, команда - {team_name}')

        try:
            id = int(input(f'Введите номер id для удаления{prompt}: ').strip())
        except ValueError:
            break

        prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'

        if id in teammate["PersonId"]:
            del teammate['PersonId'][id - 1]
            del teammate['TeamId'][id - 1]
            del teammate['FirstName'][id - 1]
            del teammate['LastName'][id - 1]
            del teammate['PersonAge'][id - 1]
            print('Удаление прошло успешно!\n')

            # если удалили всю команду:
                # не в этой версии программы...
            
        else:
            print(f'message: id номер {id} не существует!')
            error += 1
            if error >= 3:
                print('message: слишком частые попытки неправильного ввода!')
                break

def find_teammate(teammate, teams):
    def search_teammate_by_first_name(teammate, teams):
        print('---Найти по имени---')

        prompt = ''

        while True:
            first_name = input(f'Введите имя члена команды{prompt}: ').strip().capitalize()

            if first_name == '':
                break

            prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'
            count = 0

            for ind_teammate in range(len(teammate['FirstName'])):
                if first_name == teammate['FirstName'][ind_teammate]:
                    index = ind_teammate
                    team_id = teammate['TeamId'][index]
                    last_name = teammate['LastName'][index]
                    age = teammate['PersonAge'][index]

                    for ind in range(len(teams['TeamId'])):
                        if teams['TeamId'][ind] == team_id:
                            index_team = ind
                
                    team = teams['TeamName'][index_team]
                    country = teams['Country'][index_team]
                    print(f'Найден член команды: "{team}"\nИмя - {first_name}\nФамилия - {last_name}\nВозраст - {age}\nСтрана - {country}')
                    count += 1

            if count == 0:
                print(f'Имя "{first_name}" не найденно')      
    
    def search_teammate_by_last_name(teammate, teams):
        print('---Найти по фамилии---')

        prompt = ''

        while True:
            last_name = input(f'Введите фамилию члена команды{prompt}: ').strip().capitalize()

            if last_name == '':
                break

            prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'
            count = 0

            for ind_teammate in range(len(teammate['LastName'])):
                if last_name == teammate['LastName'][ind_teammate]:
                    index = ind_teammate
                    team_id = teammate['TeamId'][index]
                    first_name = teammate['FirstName'][index]
                    age = teammate['PersonAge'][index]

                    for ind in range(len(teams['TeamId'])):
                        if teams['TeamId'][ind] == team_id:
                            index_team = ind
                
                    team = teams['TeamName'][index_team]
                    country = teams['Country'][index_team]
                    print(f'Найден член команды: "{team}"\nИмя - {first_name}\nФамилия - {last_name}\nВозраст - {age}\nСтрана - {country}')


            if count == 0:
                print(f'Имя "{last_name}" не найденно')   

    def show_all_teammates_information(teammate, teams):
        print('---Вся информация по командам:---')

        for ind_team in range(len(teams['TeamId'])):
            name_team = teams['TeamName'][ind_team]
            country = teams['Country'][ind_team]
            print(f'Команда: {name_team}, страна: {country}\nСостав:')
            count = 1
            for ind_teammate in range(len(teammate['TeamId'])):
                if ind_team + 1 == teammate['TeamId'][ind_teammate]:
                    first_name = teammate['FirstName'][ind_teammate]
                    last_name = teammate['LastName'][ind_teammate]
                    age = teammate['PersonAge'][ind_teammate]
                    print(f'{count}. Имя - {first_name}, Фамилия - {last_name}, Возраст - {age}')
                    count += 1

            print('\n')
                

    def search_teammates_by_specified_letter(teammate, teams):
        print('---Найти фамилию по букве---')

        prompt = ''

        while True:
            word = input(f'Введите букву для поиска{prompt}: ').strip().capitalize()

            if word == '':
                break

            prompt = ' или нажмите "Enter", чтобы вернуться в главное меню'
            count = 0
            
            for ind_teammate in range(len(teammate['LastName'])):
                if word == teammate['LastName'][ind_teammate][0]:
                    index = ind_teammate
                    team_id = teammate['TeamId'][index]
                    first_name = teammate['FirstName'][index]
                    last_name = teammate['LastName'][index]
                    age = teammate['PersonAge'][index]

                    for ind in range(len(teams['TeamId'])):
                        if teams['TeamId'][ind] == team_id:
                            index_team = ind
                
                    team = teams['TeamName'][index_team]
                    country = teams['Country'][index_team]
                    print(f'Найден член команды: "{team}"\nИмя - {first_name}\nФамилия - {last_name}\nВозраст - {age}\nСтрана - {country}')
                    count += 1
            
            if count == 0:
                print(f'Фамилий на букву "{word}" не найденно')

    actions = {'1': search_teammate_by_first_name, '2': search_teammate_by_last_name, '3': show_all_teammates_information, '4': search_teammates_by_specified_letter}

    while True:
        navigation = input("""Введите цифру, чтобы найти тиммейта:
            1 - по имени
            2 - по фамилии
            3 - показать все команды
            4 - поиск фамилии по указанной букве
            или любой символ, чтобы вернуться в главное меню
            : """).strip()
        
        if navigation in actions:
            actions[navigation](teammate, teams)
        else:
            break

def save_changes(teammate, teams):
    import json

    with open("teammate.json", "w") as file:
        json.dump(teammate, file)

    with open("teamName.json", "w") as file:
        json.dump(teams, file)   
    
    print('Message: операция сохранения изменений прошла успешно!')
    print('\n')

go_to_action()