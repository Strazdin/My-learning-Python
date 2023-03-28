# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения).
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.
""" 
class SetNums:

    def __init__(self):
        self.queue = []

    def check_number(self, number):
        if number in self.queue:
            return True
        else:
            return False

    def add_element(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
        else:
            print(f'The number: {value} exists in the list!')
        
    def remove_element(self, number):
        if len(self.queue) > 0:
            if self.check_number(number):            
                while number in self.queue:
                    self.queue.remove(number)

                print(f'All numbers {number} removed successfully!')
            else:
                print(f'The number {number} is not in the list')
        else:
            raise Exception("Queue is Empty") 

    def show(self):
        show = input('show list first or last?\n Enter f\\l: ').strip().capitalize()

        if show == 'L':
            for item in self.queue[::-1]:
                print(item)
        else:
            for item in self.queue:
                print(item)
                    
    def replace_number(self, old, new):
        if self.check_number(old):
            user_choice = input('заменить только первое вхождение (first) или все вхождения (all)\nEnter f\\a: ').strip().capitalize()

            for i in range(len(self.queue)):
                if self.queue[i] == old:
                    self.queue[i] = new

                    if user_choice == 'F':
                        break                
        else:
            print(f'The number {old} is not in the list')



set_nums = SetNums()


while True:
    try:
        number = int(input('Enter a number: '))
        set_nums.queue.insert(0, number)
    except ValueError:
        break

while True:
    try:
        user_choice = int(input('1. Add element\n2. Remove element\n3. Show list\n4. Replace number\n5. Check number\nEnter digit (0-5), 0 - exit: '))

        if user_choice == 1:
            number = int(input('Enter a number: '))
            set_nums.add_element(number)
        elif user_choice == 2:
            number = int(input('Enter number to delete: '))
            set_nums.remove_element(number)
        elif user_choice == 3:
            set_nums.show()
        elif user_choice == 4:
            old = int(input('Enter the old number: '))
            new = int(input('Enter a new number: '))
            set_nums.replace_number(old, new)
        elif user_choice == 5:
            number = int(input('Enter a number to check: '))

            if set_nums.check_number(number):
                print(f'The number: {number} exists in the list')
            else:
                print(f'The number {number} is not in the list')
        elif user_choice == 0:
            print('Exit')
            break
    except ValueError:
        print('Error! Enter digit (0-5)!') """

""" Задание 2
Реализуйте класс стека для работы со строками (стек
строк).
Стек должен иметь фиксированный размер.
Реализуйте набор операций для работы со стеком:
■ помещение строки в стек;
■ выталкивание строки из стека;
■ подсчет количества строк в стеке;
■ проверку пустой ли стек;
■ проверку полный ли стек;
■ очистку стека;
■ получение значения без выталкивания верхней строки
из стека.
При старте приложения нужно отобразить меню с
помощью, которого пользователь может выбрать необходимую операцию. """

class Stack():
    def __init__(self, max_size = 9):
        self.max_size = max_size
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True

    def is_full(self):
        if len(self.data) >= self.max_size:
            return True
        
    def get_length(self):
        return len(self.data)

    def push(self, text):
        if not self.is_full():
            self.data.append(text)
            return text
        else:
            raise Exception('Стек полный! Нельзя добавить в полный стек!')

    def pop(self):
        if not self.is_empty():
            output = self.data[len(self.data) -1]
            del self.data[len(self.data) -1]
            return output
        else:
            raise Exception('Стек пустой! Нельзя удалить из пустого стека!')
        
    def clean(self):
        while (not self.data == []):
            self.data.pop()

        print('Стек очищен!')

    def pull(self, index):
        try:
            return self.data[index]
        except IndexError:
            print('Error message')

stack_str = Stack()

while True:
    user_choice = int(input('1. Помещение строки в стек\n2. Выталкивание строки из стека\n3. Подсчет количества строк в стеке;\n4. Пустой ли стек?\n5. Полный ли стек?\n6. Очистка стека\n7. Получение значения без выталкивания верхней строки из стека.\nEnter digit (0-7), 0 - exit: '))

    if user_choice == 1:
        text = input('Введите текст: ')
        print(f'Строка \'{stack_str.push(text)}\' помещена в стек')
    elif user_choice == 2:
        print(f'\'{stack_str.pop()}\' уходит из стека')
    elif user_choice == 3:
        print(f'{stack_str.get_length()} - кол-во строк в стеке')
    elif user_choice == 4:
        if stack_str.is_empty():
            print('Стек пустой')
        else:
            print('Стек не пустой')
    elif user_choice == 5:
        if stack_str.is_full():
            print('Стек полный')
        else:
            print('Стек не полный')

    elif user_choice == 6:
        stack_str.clean()
    elif user_choice == 7:
        index = int(input('Введите индекс: '))
        result = stack_str.pull(index)
        print(f'Резульат по индексу {index}: {result}')
    else:
        print('Exit')
        break

""" Задание 3
Измените стек из второго задания, таким образом,
чтобы его размер был нефиксированным """

class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        
    def get_length(self):
        return len(self.data)

    def push(self, text):
        self.data.append(text)
        return text

    def pop(self):
        if not self.is_empty():
            output = self.data[len(self.data) -1]
            del self.data[len(self.data) -1]
            return output
        else:
            raise Exception('Стек пустой! Нельзя удалить из пустого стека!')