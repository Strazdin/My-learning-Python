class Date:
    def __init__(self, year, month, day):
        if self.check_type(year, int):
            self.__year = year
        if self.check_type(month, int):
            self.__month = month
        if self.check_type(day, int):
            self.__day = day

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month
    
    @property
    def day(self):
        return self.__day
    
    @staticmethod
    def check_type(arg, type):
        if isinstance(arg, type):
            return True
        else:
            raise TypeError(f'Error message (Expected type {type})')

    @year.setter
    def year(self, year):
        if self.check_type(year, int):
            self.__year = year

    @month.setter
    def month(self, month):
        if self.check_type(month, int):
            if 0 < month <= 12:
                self.__month = month
            else:
                raise ValueError('Error message')

    @day.setter
    def day(self, day):
        days = self.days_in_month()
        
        if self.check_type(day, int):
            if 0 < day <= days:
                self.__day = day
            else:
                raise ValueError('Error message')

    def is_leap_year(self, year=None):
        year = year if year else self.__year

        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def days_in_month(self, month=None, year=None):
        month = month if month else self.__month

        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28
        
    def next_day(self):
        if self.__day < self.days_in_month(self):
            self.__day += 1
        elif self.__month < 12:
            self.__day = 1
            self.__month += 1
        else:
            self.__day = 1
            self.__month = 1
            self.__year += 1

    def set_date(self, string):
        import re
        pattern_str = r'^\d{4}.\d{2}.\d{2}$'

        if re.match(pattern_str, string):
            day, month, year = string[8:], string[5:7], string[:4]
            self.month = int(month)
            self.day = int(day)
            self.year = int(year)
        else:
            raise ValueError('Error message')
        
    def __str__(self):
        return f'{self.year}.{self.month}.{self.day}'

date1 = Date(2023, 3, 7)
print(date1.day)
print(date1)
date1.next_day()
# date1.day = 'bla-bla'
print(date1.day)
date1.set_date('2023.03.22')
print(date1)