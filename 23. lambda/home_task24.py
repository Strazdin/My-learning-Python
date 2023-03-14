#Задание 1.

bstr = 'abcdefghijklmnopqrstuvwxyz'
b = lambda str: ''.join([string for string in bstr if string not in 'aeiouAEIOU'])
print(b(bstr))

#Задание 2.

bstr = 'abcdefghijklmnopqrstuvwxyz1'
b = lambda str: str.isalpha()
print(b(bstr))

#Задание 3.

from functools import reduce
nums = [1, 2, 3, 5, 7, 5, 9, 15]
mult_num = reduce((lambda x, y: x * y), nums)
print(mult_num)

#Задание 4.

strings = ['dfrgs', 'tenet', 'dkdkdkle', 'fdf']
new_list = lambda lst: ([string for string in strings if str(string) == str(string)[::-1]])
print(new_list(strings))

#Задание 5.

digit = 67
res = lambda x: all([x % i != 0 for i in range(2, (x // 2) + 1)])
print(res(digit))

#Задание 6.

fact = lambda n: 1 if n == 0 else n * fact(n - 1)
print(fact(5))


