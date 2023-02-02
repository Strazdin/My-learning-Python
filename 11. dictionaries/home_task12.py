
# Модуль 8. Кортежи, множества, словари

""" Задание 2
Создайте программу «Англо-французский словарь». 
Нужно хранить слово на английском языке и его перевод 
на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте 
словарь для хранения информации. """

# Делаю Англо-русский словарь, еще одно задание делать не стал, т.к 3 и 4 подобно этому и хотелось сделать что-то одно, +/- полноценное
# Многое было написано методом гугления, т.к многие темы еще не прошли, наверное.
# Код переписывался раза три, т.к заранее не распланировал все, мне хотелось улучшить читаемость кода для проверки
# и тестировался тоже несколько раз на этапах переписывания, вроде бы все норм, но
# нашел одну наверное прям критическую ошибку под конец, написал об этом ниже в виде вопроса (75 строка кода)
# Далее комментарии по коду:

# Создание файла "dictionary.json" и его заполнение словарем.
def get_dictionary_file():
    import json
    import requests
    from bs4 import BeautifulSoup

    rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
    root = BeautifulSoup(rs.content, 'html.parser')

    en_ru_items = {}

    for tr in root.select('tr[onmouseover]'):
        td_list = [td.text.strip() for td in tr.select('td')]

        if len(td_list) != 9 or not td_list[1] or not td_list[5]:
            continue

        en = td_list[1]
        ru = td_list[5]

        en_ru_items[en] = ru

    with open("dictionary.json", "w") as file:
        json.dump(en_ru_items, file)    

    # print(len(en_ru_items), en_ru_items)


# create_dictionary возвращает словарь (dict) en-ru, записанный с ранее созданного файла
# Внимание! Если файл dictionary.json уже существует, то выше описанная функция вызываться не будет
def create_dictionary() -> dict:
    import json
    import os.path

    file_path = "./dictionary.json"
    
    if not os.path.isfile(file_path):
        get_dictionary_file()

    dictionary = {}

    with open("dictionary.json") as file:
        dictionary = json.load(file)

    return dictionary

# Меню. Здесь происходит выбор пользователя по функционалу: add, delete, find, replace, save.
# Его выбор в виде введеной строки вызовет функцию, которая соответствует его логическому выбору (хранится в переменной func_call)
def show_menu_dictionary(dictionary):
    error_variable = 0

    while error_variable <= 3:
        func_call = {'add': add_word_to_dictionary, 'delete': delete_word_in_dictionary, 'find': find_word_in_dictionary, 'replace': replace_word_in_dictionary, 'save': save_changes_to_dictionary}
        
        navigation = input('\t\tWelcome to english russian dictionary!\n\t\t\t\t\t\tМеню:\nAdd - добавление слова или варианта перевода существующего\nDelete - удалить слово или один из вариантов веревода\nFind - найти перевод слова\nReplace - заменить вариант перевода\nSave - сохранить все изменения\nExit - выйти из программы\n\nВведите команду на английском языке: ').strip().lower()

        if navigation in func_call:
            func_call[navigation](dictionary)
        # Вопрос. Является ли нормальной практикой делать переходы через функциям? Столкнулся с проблемой: если немного полазить в программе, и потом ввести тут 'выход', то программа не закроется, а вызовется опять эта же функция show_menu_dictionary, грубо говоря столько же раз сколько она была вызвана. Да, я добавил много где вызов этой функции. Не совсем понимаю как это работает...
        # Лучше тогда все через циклы надо было делать? Или обязательно чтобы функции return имели, чтобы они завершила свою работу.
        elif navigation == 'exit' or navigation == 'e':
            print('Message: До скокрой встречи!')
            break
        else:
            error_variable += 1

            if error_variable != 4:
                print('Message: ошибка ввода')
            else:
                print('Message: обнаружены подозрительные попытки ввода. Программа вынуждена закрыться')

            print("\n")

# Далее идут так называемые служебные функции, сделаны для того, чтобы убрать повторяемый код, сделать его более читаемым. ()
# 
def exit_to_menu_or_continue_operation(skip_option) -> bool:
    print("\n" * 2)
    if skip_option != 0:
        exit_or_continue = input('Продолжить операцию или выйти в меню?\nВведите +\-\n').strip()
        print("\n" * 2)
        return exit_or_continue == "+"

# 
def add_ru_word_to_dictionary(en_word: str, dictionary: dict, is_english_word_exist: bool, skip_option = 0):
    def exit_or_continue_add_ru_word(en_word, ru_word, skip_option_2) -> bool:
        if skip_option_2 != 0:
            ru_word_add_and_stop = input(f'Добавить еще одно значение перевода слова {en_word}?\n+\-: ').strip()
            print("\n" * 2)
            return ru_word_add_and_stop == "+"
        
    ru_word = dictionary[en_word] if is_english_word_exist else ''

    while exit_or_continue_add_ru_word(en_word, ru_word, skip_option) or skip_option == 0:
        ru_word_one = input(f'Введите перевод английского слова {en_word} на русский: ').lstrip().rstrip()

        if is_word_correct_input(ru_word_one, language = 'ru'):
            if ru_word_one not in ru_word:
                ru_word += ', ' + ru_word_one if is_english_word_exist else ru_word_one + ', '                           
            else:
                print('Message: ошибка! Такой перевод уже существует!')

            dictionary[en_word] = ru_word if is_english_word_exist else ru_word
            print(f'Перевод слова {en_word} - {ru_word_one} успешно добавлен в словарь!')
        else:
            break

        skip_option = 1
    
    if not is_english_word_exist:
        ru_word = ru_word[:-2]
        dictionary[en_word] = ru_word

# 
def is_word_correct_input(word: str, language) -> bool:
    def show_message_error():
        print('Message: Ошибка! Введенный текст не может быть пустым или слишком длинным.\nА также должен соответстовать логике словаря: английское слово или русский перевод.')
        
    def is_english_word(en_word) -> bool:
        import string
        char_set = string.ascii_letters

        return all((True if x in char_set else False for x in en_word))

    def is_russian_word(ru_word) -> bool:
        alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"," ","-","0","1","2","3","4","5","6","7","8","9"]

        for one_char in ru_word.lower():
            if one_char not in alphabet:
                return False
            
        return True
    
    def check_length_english_word(en_word) -> bool:
        return len(en_word) <= 45 and len(en_word) != 0

    def check_translation_length(ru_word) -> bool:
        return len(ru_word) <= 100 and len(ru_word) != 0
    
    if language == 'en':
        if check_length_english_word(word) and is_english_word(word):
            return True
    elif language == 'ru':
        if check_translation_length(word) and is_russian_word(word):
            return True
        
    show_message_error()
    return False

# Далее идет функционал: add, delete, find, replace, save
def add_word_to_dictionary(dictionary):
    skip_option = 0

    while exit_to_menu_or_continue_operation(skip_option) or skip_option == 0:
        en_word = input('Введите английское слово, которое будет добавлено в словарь или,\nесли оно существует в словаре, будет возможность добавить перевод к этому слову\n: ').lstrip().rstrip()#.lower()
        
        if is_word_correct_input(en_word, language = 'en'):
            if en_word in dictionary:
                add_translation_or_no = input(f'Слово {en_word} уже есть в словаре!\nЕго перевод: {dictionary[en_word]}\nЖелаете добавить вариант перевода?\nВведите +\-\n: ').strip()
            
                if add_translation_or_no == "+":
                    add_ru_word_to_dictionary(en_word, dictionary, is_english_word_exist = True)

            else:
                add_translation_or_no = input(f'Слова {en_word} нет в словаре. \nЖелаете добавить вариант перевода?\nВведите +\-\n: ').strip()
                
                if add_translation_or_no == "+":
                    add_ru_word_to_dictionary(en_word, dictionary, is_english_word_exist = False)

        skip_option = 1
    

def delete_word_in_dictionary(dictionary):
    skip_option = 0
        
    while exit_to_menu_or_continue_operation(skip_option) or skip_option == 0:
        en_word = input('Введите английское слово, которое будет удалено из словаря или удален один из его переводов: ').lstrip().rstrip()
        print("\n" * 2)
        
        if en_word in dictionary:
            delete_word_or_delete_translate = input('Введите "+", чтобы удалить слово\nВведите "-", чтобы удалить один из его переводов\n:').strip()
            print("\n" * 2)

            if delete_word_or_delete_translate == "+":
                dictionary.pop(en_word)
                print(f'Message: слово {en_word} успешно удалено!')
            elif delete_word_or_delete_translate == "-":
                ru_word = dictionary[en_word].split(', ')
                error_variable = 0

                while True:
                    if len(ru_word) > 1:
                        ru_word_delete = input(f'Слово {en_word} с количеством переводов: {len(ru_word)}.\nА именно: {dictionary[en_word]}\nВведите слово, которое нужно удалить или "-", чтобы вернуться в меню удаления слов: ').lstrip().rstrip()

                        if ru_word_delete in ru_word:
                            for word in ru_word:
                                if word.lstrip().rstrip() == ru_word_delete:
                                    ru_word.remove(word)
                                    print(f'Message: слово "{word}" удалено!')
                                    print("\n" * 2)
                                    ru_word = ", ".join(ru_word)
                                    dictionary[en_word] = ru_word
                                    ru_word = dictionary[en_word].split(', ')
                        else:
                            if ru_word_delete == '-':
                                break
                            else:
                                error_variable += 1

                                if error_variable == 4:
                                    print('Message: обнаружен подозрительный ввод.')
                                    break
                                else:
                                    print('Message: ошибка в слове или такого перевода нет в словаре!')
                    else:
                        print(f'Message: слово {en_word} имеет лишь один единственный перевод, удалить один перевод невозможно.\nЭто слово можно только удалить целиком!')
                        break
            else:
                print('Message: пропуск операции удаления...')
        else:
            print(f'Message: слова {en_word} нет в словаре')

        skip_option = 1

def find_word_in_dictionary(dictionary):
    skip_option = 0
    
    while exit_to_menu_or_continue_operation(skip_option) or skip_option == 0:
        en_word = input('Введите английское слово, которое будет переведено на русский: ')
        print("\n" * 2)

        if en_word in dictionary:
            print(f'Перевод: {en_word} - {dictionary[en_word]}')
        else:
            print(f'Message: Слова {en_word} нет в словаре')
            
        skip_option = 1

def replace_word_in_dictionary(dictionary):
    skip_option = 0
    
    while exit_to_menu_or_continue_operation(skip_option) or skip_option == 0:
        en_word = input('Введите английское слово, чей перевод хотите заменить: ')
        print("\n" * 2)

        if en_word in dictionary:
            ru_word = dictionary[en_word].split(', ')
            error_variable = 0

            while True:
                ru_word_replace = input(f'Слово {en_word} с количеством переводов: {len(ru_word)}.\nА именно: {dictionary[en_word]}\nВведите слово, которое нужно заменить или "-", чтобы вернуться в меню замены слов: : ').lstrip().rstrip()

                if ru_word_replace in ru_word:
                    for word in ru_word:
                        if word.lstrip().rstrip() == ru_word_replace:
                            ru_word.remove(word)
                            ru_word_new = input(f'Message: слово "{word}" удалено! Введите перевод слова "{en_word}": ')
                            if is_word_correct_input(ru_word_new, language = 'ru'):
                                ru_word.append(ru_word_new)
                                ru_word = ", ".join(ru_word)
                                dictionary[en_word] = ru_word
                                ru_word = dictionary[en_word].split(', ')
                                print('\nMessage: операция замены перевода прошла успешно!')
                else:
                    if ru_word_replace == '-':
                        break
                    else:
                        error_variable += 1

                        if error_variable == 4:
                            print('\nMessage: обнаружен подозрительный ввод.')
                            break
                        else:
                            print('\nMessage: ошибка в слове или такого перевода нет в словаре!')
        else:
            print(f'Message: слова {en_word} нет в словаре')
            
        skip_option = 1

def save_changes_to_dictionary(dictionary):
    import json

    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file)   
    
    print('Message: операция сохранения изменений прошла успешно!')
    print('\n')

# Запуск словаря
show_menu_dictionary(create_dictionary())
