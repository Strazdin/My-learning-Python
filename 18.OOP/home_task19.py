""" Тема: Статические методы
Задание 1
К уже реализованному классу «Дробь» добавьте статический метод, который при вызове возвращает количество созданных объектов класса «Дробь». """

class Fraction:
    __counter = 0

    def __init__(self,numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__counter += 1

    def show_fraction(self):
        print(f'{self.numerator}/{self.denominator}')
        pass
    
    def reset(self):
        self.numerator = int(input('числитель: '))
        self.denominator = int(input('знаменатель: '))
    
    def sum(self, another: "Fraction"):
        return Fraction(self.numerator + another.numerator, self.denominator + another.denominator)

    @staticmethod
    def get_counter():
         return Fraction.__counter
    
num1 = Fraction(2, 4)
num2 = Fraction(9, 3)
c = num1.sum(num2)

# print(c.numerator, '/', c.denominator)
print(Fraction.get_counter())

""" Задание 2
Создайте класс для конвертирования температуры из 
Цельсия в Фаренгейт и наоборот. У класса должно быть 
два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также 
класс должен считать количество подсчетов температуры и 
возвращать это значение с помощью статического метода. """

class Temperature:
    __counter = 0

    @staticmethod
    def celsius_to_fahrenheit(t):
        Temperature.__counter += 1
        return round(9 / 5) * t + 32

    @staticmethod
    def fahrenheit_to_celsius(t):
        Temperature.__counter += 1
        return round(5 / 9) * (t - 32)

    @staticmethod
    def get_counter():
         return Temperature.__counter
    
print(Temperature.celsius_to_fahrenheit(100))
print(Temperature.fahrenheit_to_celsius(100))
print(Temperature.get_counter())

""" Задание 3
Создайте класс для перевода из метрической системы 
в английскую и наоборот. Функциональность необходимо 
реализовать в виде статических методов. Обязательно 
реализуйте перевод мер длины. """

class lengthSystem:
    @staticmethod
    def metric_to_english(length):
        inch = 2.5#см
        foot = 30.5#см
        yard = 0.9#м
        mile = 1.6#км

        res = f'{length} метров = {round(length * 100 / inch, 2)} дюймов, {round(length * 100 / foot, 2)} футов, {round(length / yard, 2)} ярдов, {round(length / 1000 / mile, 2)} милей'
        return res

    @staticmethod
    def english_to_metric(length):
        foot_cm = 30.5#см
        foot_m = 0.305#м
        foot_mm = 305#mm
        foot_km = 0.0003#км
        res = f'{length} футов = {round(length * foot_m, 2)} метров, {round(length * foot_mm, 2)} миллиметров, {round(length * foot_cm, 2)} сантиметров, {round(length * foot_km, 2)} километров'
        return res

print(lengthSystem.metric_to_english(100))
    
print(lengthSystem.english_to_metric(100))