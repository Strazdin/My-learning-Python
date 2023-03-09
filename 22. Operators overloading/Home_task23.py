""" Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей
(операция = =);
■ Сравнения длин двух окружностей (операции >, <,
<=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=). """

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def circ_len(self):
        return self.radius * 3.14 * 2
    
    def __eq__(self, other): # ==
        return self.radius == other.radius

    def __lt__(self, other): # <
        return self.circ_len() < other.circ_len()

    def __le__(self, other): # <=
        return self.circ_len() <= other.circ_len()

    def __gt__(self, other): # >
        return self.circ_len() > other.circ_len()

    def __ge__(self, other): # >=
        return self.circ_len() >= other.circ_len()
    
    def __add__(self, num: int): # +
        return Circle(self.radius + num)

    def __iadd__(self, num: int): # +=
        self.radius += num

    def __sub__(self, num: int): # -
        return Circle(self.radius - num)

    def __isub__(self, num: int): # -=
        self.radius -= num

    def __str__(self):
        return f'{self.radius}'

a = Circle(5)
b = Circle(3)

# не понял как вызвать +=, -= тут
print(a + 5)
print(b - 3)
print(a < b)
print(a <= b)
print(a == b)
print(a > b)
print(a >= b)

""" Задание 2
Создайте класс Complex (комплексное число). Более
подробно ознакомиться с комплексными числами можно
по ссылке.
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /). """

class Complex:

    def __init__(self, real, imag):
        self.real = real #x1, other.real x2
        self.imag = imag #y1, other.imag y2

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.real)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.real)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - (self.imag * other.imag), self.imag * other.real + self.imag * other.imag)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - (self.imag * other.imag), self.imag * other.real + self.imag * other.imag)
    
    def __truediv__(self, other):
        return Complex((self.real * other.real + self.imag + other.imag) / other.real ** 2 + other.imag ** 2, (self.imag * other.real - self.real + other.imag) / other.real ** 2 + other.imag ** 2)
    
    def __str__(self):
        return f'{self.real} + {self.imag}i'
    
a = Complex(5, 2)
b = Complex(3, 7)

print(a + b)
print(a * b)
print(a / b)

""" Задание 3
Вам необходимо создать класс Airplane (самолет).
С помощью перегрузки операторов реализовать:  """
""" ■ Проверка на равенство типов самолетов (операция
= =);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
< <= >=). """

class Airplane:
    def __init__(self, airplane_type, max_passengers, passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers

        if passengers > max_passengers:
            raise Exception('Error')
        else:
            self.passengers = passengers

    def __eq__(self, other: 'Airplane'):
        return self.airplane_type == other.airplane_type
    
    def __add__(self, num: int): # +
        return Airplane(self.airplane_type, self.max_passengers, self.passengers + num)

    def __iadd__(self, num: int): # +=
        self.passengers += num

    def __sub__(self, num: int): # -
        return Airplane(self.airplane_type, self.max_passengers, self.passengers - num)

    def __isub__(self, num: int): # -=
        self.passengers -= num

    def __lt__(self, other: 'Airplane'): # <
        return self.max_passengers < other.max_passengers

    def __le__(self, other: 'Airplane'): # <=
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other: 'Airplane'): # >
        return self.max_passengers > other.max_passengers

    def __ge__(self, other: 'Airplane'): # >=
        return self.max_passengers >= other.max_passengers
    
    def __str__(self):
        return f'Type {self.airplane_type}, Passengers {self.passengers}, max {self.max_passengers}'
    
d = Airplane('type1', 100, 80)
e = Airplane('type2', 100, 50)

print(d == e)
print(d < e)
print(d + 20)
print(d - 5)

    
""" Задание 4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
■ Проверка на равенство площадей квартир (операция
==);
■ Проверка на неравенство площадей квартир (операция !=);
■ Сравнение двух квартир по цене (операции > < <= >=). """

class Flat:
    def __init__(self, s, cost):
        self.s = s
        self.cost = cost

    def __eq__(self, other: 'Flat'):
        return self.s == other.s
    
    def __lt__(self, other: 'Flat'): # <
        return self.cost < other.cost

    def __le__(self, other: 'Flat'): # <=
        return self.cost <= other.cost

    def __gt__(self, other: 'Flat'): # >
        return self.cost > other.cost

    def __ge__(self, other: 'Flat'): # >=
        return self.cost >= other.cost
    
    def __str__(self):
        return f'Площадь {self.s}, Цена {self.cost}'
    
flat1 = Flat(100, 1)
flat2 = Flat(200, 4)

print(flat1 != flat2)
print(flat1 == flat2)
print(flat1 <= flat2)