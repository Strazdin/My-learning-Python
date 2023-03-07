from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, coords):
        self.coords = coords

    def show(self):
        print(f'Фигура {self.__class__.__name__}')
        print('Ее св-ва: ')
        for name, value in self.__dict__.items():
            print(f'{name} = {value}')

    def save(self, file_name):
        count = 0
        
        with open(f'{file_name}.txt', 'a', encoding = 'UTF-8') as f:
            f.write(self.__class__.__name__ + ': ')

            for name, value in self.__dict__.items():
                count += 1
                f.write(name + ' - ' + str(value) + ', ') if count < len(self.__dict__) else f.write(name + ' - ' + str(value) + ';')
    
    @staticmethod
    def load(file_name) -> list:
        with open(f'{file_name}.txt', 'r',  encoding = 'utf-8') as f:
            data = f.read()
            values = []
            values = data.split(";")
            return values

class Square(Shape):
    def __init__(self, coords, l):
        Shape.__init__(self, coords)
        self.l = l

class Rectangle(Shape):
    def __init__(self, coords, a, b):
        if a == b:
            raise Exception('Error mesage')
        else:
            Shape.__init__(self, coords)
            self.a = a
            self.b = b

class Cirсle(Shape):
    def __init__(self, coords, radius):
        Shape.__init__(self, coords)
        self.radius = radius

class Ellipse(Shape):
    def __init__(self, coords, a, b):
        if a == b:
            raise Exception('Error mesage')
        else:
            Shape.__init__(self, coords)
            self.a = a
            self.b = b

file_name = 'file'
figure_list = []

a = Square((4, 3), 10)
b = Rectangle((1, 5), 2, 3)
c = Cirсle((2, 3), 10)
d = Ellipse((4, 6), 4, 5)

a.save(file_name)
b.save(file_name)
c.save(file_name)
d.save(file_name)

figure_list.append(a)
figure_list.append(b)
figure_list.append(c)
figure_list.append(d)

new_figure_list = Shape.load(file_name)

for i in range(len(new_figure_list)):
    print(new_figure_list[i])