""" Задание 1
Необходимо отсортировать первые две трети списка 
в порядке возрастания, если среднее арифметическое 
всех элементов больше нуля; иначе — лишь первую треть. 
Остальную часть списка не сортировать, а расположить 
в обратном порядке. """

# Комментарии по функциям:

# Функция split_length_of_list_into_two_parts принимает список и производит деление длины списка на 2/3 и 1/3 части и возвращает список с этими частями. Нулевой индекс[0] соответствует 2/3 части, [1] - 1/3 части, [2] - полной длине переданного списка.
# Эта функция прежде всего сделана для того, чтобы равномерно разделить список на две части в тех случаях, когда длина списка не делится на 3 нацело.

# Функция is_arithmetic_mean_greater_than_zero принимает список и возвращает True, если среднее арифметическое всех чисел в списке БОЛЬШЕ нуля и возвращает False, если среднее арифметическое МЕНЬШЕ или РАВНО нулю.

# Функция reverse_list имеет три параметра - список, и две "точки": начало и конец, которые передаются в виде индексов списка от которой начинается реверсия (начало) и заканчивается (конец в данной задаче - полная длина списка). Функция изменяет существующий (переданный) список.

# Функции define_index_partition и sort_list реализуют алгоритм быстрой сортировки (соответствует схеме Хоара).

# Также sort_list вызывает все остальные функции для решения поставленной задачи. 


def split_length_of_list_into_two_parts(lenght_list):
    start_and_end_list = []

    if lenght_list % 3 == 0:
        start_and_end_list = [lenght_list // 3 * 2, lenght_list // 3]
    elif lenght_list % 3 == 1:
        start_and_end_list = [lenght_list // 3 * 2 + 1, lenght_list // 3]
    elif lenght_list % 3 == 2:
        start_and_end_list = [lenght_list // 3 * 2 + 1, lenght_list // 3 + 1]

    start_and_end_list.append(lenght_list)
    return start_and_end_list

def is_arithmetic_mean_greater_than_zero(list_numbers):
    sum = 0
    
    for i in range(len(list_numbers)):
        sum += list_numbers[i]

    arithmetic_mean = sum // len(list_numbers)
    return arithmetic_mean > 0

def reverse_list(list_numbers, start, end):
    for i in range(start, end):
        last_item = list_numbers.pop()
        list_numbers.insert(i, last_item)
 
def define_index_partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        
        while nums[i] < pivot:
            i += 1

        j -= 1

        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def sort_list(list_numbers):
    def _sort_list(items, low, high):
        if low < high:
            split_index = define_index_partition(items, low, high)
            _sort_list(items, low, split_index)
            _sort_list(items, split_index + 1, high)

    list_lenght = split_length_of_list_into_two_parts(len(list_numbers))

    if is_arithmetic_mean_greater_than_zero(list_numbers):
        _sort_list(list_numbers, 0, list_lenght[0] - 1)
        reverse_list(list_numbers, list_lenght[0], list_lenght[2])
    else:
        _sort_list(list_numbers, 0, list_lenght[1] - 1)
        reverse_list(list_numbers, list_lenght[1], list_lenght[2])

import random

random_list_of_numbers = [random.randint(-20, 20) for i in range(0, 8)]
print( 'Рандом: ', random_list_of_numbers )
sort_list(random_list_of_numbers)
print( 'Сортировка: ', random_list_of_numbers )

# Напишите, пожалуйста, сыграли ли роль на быстроту проверки и на понимание программы комментарии по функциям и в целом мой написанный код.
# Интересует как писать комментарии по написанному коду, чтобы другой человек мог быстрее понять как он работает. И что в целом лучше писать в комментариях.
# Для решения задачи выбрал алгоритм быстрой сортировки из того, что нашел в интернете и ранее изученного т.к во-первых он быстрый:)
# во-вторых я увидел как его можно оптимизировать под решение этой задачи.
# Но в саму работу алгоритма досканально не вникал, лишь скопировал и понял, что нужно там изменить, чтобы на выходе "ответ был верный".
# Вопрос:
# Есть ли какие-то методы тестирования, чтобы, грубо говоря, не зная как работает код, а лишь зная что должно пойти и выйти узнать работает ли код правильно или нет.
# Написанный код пришлось тестировать как, наверное, говориться вручную. Это каждый раз запускать его при разных значениях и сверять ответ с условием задачи.

""" Задание 2
Написать программу «успеваемость». Пользователь 
вводит 10 оценок студента. Оценки от 1 до 12. Реализовать 
меню для пользователя:
■ Вывод оценок (вывод содержимого списка);
■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
■ Выходит ли стипендия (стипендия выходит, если 
средний бал не ниже 10.7);
■ Вывод отсортированного списка оценок: по возрастанию или убыванию. """

def choice_to_exit_or_continue():
    next_or_stop = input("\nВернуться в меню?\nY/N:").strip().capitalize()

    if next_or_stop == 'Y':
        show_menu_for_user(academic_performance)
    else:
        print('\nВышли из меню')

def show_academic_performance(academic_performance):
    print('\nУспеваемость: ' + ', '.join(str(value) for value in academic_performance) + '.')
    
    choice_to_exit_or_continue()

def change_grade(academic_performance):
    index_number = int(input('Введите порядковый номер (1 - 12) в списке оценок: '))
    new_grade = int(input('Введите новую оценку: '))
    academic_performance[index_number - 1] = new_grade

    choice_to_exit_or_continue()

def is_student_scholarship(academic_performance):
    sum = 0
    
    for i in range(len(academic_performance)):
        sum += academic_performance[i]

    arithmetic_mean = sum / len(academic_performance)
    arithmetic_mean = round(arithmetic_mean, 1)
    print('Средний балл: ' + str(arithmetic_mean) )

    if arithmetic_mean >= 10.7:
        print('Стипендия выходит!')
    else:
        print('Стипендии не положено.')

    choice_to_exit_or_continue()

def sort_list_grade(spisok):
    sort_selection = int(input('Введите:\n1 - для сортировки списка оценок по возрастанию,\n2 - по убыванию.\n: '))
    swapped = True

    # Решил сделать сортировку пузырьком и заодно усовершенствованный метод в нем по заданию 3.
    # Хоть список и состоит из 10 элементов, думаю, небольшое улучшение не повредит и заодно избавлюсь от написания одинакового кода в двух заданиях)

    while swapped:
        swapped = False
        for i in range(len(spisok) - 1):
            if sort_selection == 1:
                if spisok[i] > spisok[i + 1]:
                    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                    swapped = True
            else:
                if spisok[i] < spisok[i + 1]:
                    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                    swapped = True


    choice_to_exit_or_continue()


def show_menu_for_user(academic_performance):
    option = int(input('Введите цифры 1-4 чтобы вызвать опции:\n1 - показать все оценки\n2 - изменить оценку (пересдача) \n3 - получит ли стипендию?\n4 - показать отсортированный список оценок\nВыход из меню - ввод любых других символов\n: '))

    if option == 1:
        show_academic_performance(academic_performance)
    elif option == 2:
        change_grade(academic_performance)
    elif option == 3:
        is_student_scholarship(academic_performance)
    elif option == 4:
        sort_list_grade(academic_performance)
    else:
        print('\nВышли из меню')

print('-------------------------------------------------')

# Различные варианты заполнения списка (делал для тестирования):

# academic_performance = [12 for i in range(0, 10)]
academic_performance = [random.randint(1, 12) for i in range(0, 10)]
# academic_performance = [10, 2, 3, 4, 5, 6, 7, 8, 9 , 1]

# Закомментированный пользовательский ввод:

""" academic_performance = []
for i in range(10):
    academic_performance.append(int(input(f'Введите оценку студента №{i + 1} от 1 до 12: '))) """

show_menu_for_user(academic_performance)

# Лень было расписывать еще различные проверки того, что введет пользователь. Думаю, в задаче не в этом суть...

""" Задание 3
Написать программу, реализующую сортировку списка 
методом усовершенствованной сортировки пузырьковым 
методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если 
это количество равно нулю, то продолжать сортировку 
нет смысла — список отсортирован. """

# Усовершенствованная реализация сортировки пузырьковым методом находится в задании №2 (sort_list_grade - функция)