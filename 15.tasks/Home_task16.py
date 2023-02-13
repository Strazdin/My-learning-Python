# 3.
# Вам дана матричная сетка размера m x n,
# состоящая из положительных целых чисел.
#
# Выполняйте следующую операцию, пока сетка не станет пустой:
#
# Удалите элемент с наибольшим значением из каждой строки.
# Если существует несколько таких элементов, удалите любой из них.
# Добавьте к ответу максимальный из удаленных элементов.
# Обратите внимание, что количество столбцов уменьшается на
# один после каждой операции.
#
# Верните ответ после выполнения операций, описанных выше.
#
# Пример: [[1, 2, !4!], => [[1, !2!], => [[!1!], => [[],
#          [!3!, 3, 1]] =>  [!3!, 1]] =>  [!1!]] =>  []]
#             0 + 4   ||   4 + 3  ||  7 + 1 => Ответ: 8

import random

m = int(input('rows = '))
n = int(input('columns = '))

grid = [[random.randint(1, 10) for j in range(n)] for i in range(m)]
print('Grid m*n:')

for i in range(m):
    print(grid[i])

max_list = []
max_list2 = []
for j in range(n):
    for i in range(m):
        max_int = max(grid[i])
        max_list.append(max_int)
        grid[i].remove(max_int)
        print(f'...max in row №{i}...')
        print(max_list)
    max_list2.append(max(max_list))
    print('max list 2: ')
    print(max_list2)
    max_list.clear()
    print('grid: ')
    print(grid)

print(f'Ответ: {sum(max_list2)}')

# 8.
# Вам дана целочисленная матричная сетка размера n x n.
#
# Создайте целочисленную матрицу max_local размера
# (n - 2) x (n - 2), такую, что:
#
# max_local[i][j] равно наибольшему значению матрицы
# 3 x 3 в сетке с центром вокруг строки i + 1 и столбца j + 1.
# Другими словами, мы хотим найти наибольшее значение
# в каждой непрерывной матрице 3 x 3 в сетке.
#
# Верните сгенерированную матрицу.
import random

n = int(input('n = '))

grid = [[random.randint(0, 40) for j in range(n)] for i in range(n)]

for i in range(n):
    print(grid[i])

list3x3 = []
max_list = []
list_result = []

for i in range(n - 2):
    center_row = i + 1

    for j in range(n - 2):
        center_column = j + 1

        for r in range(center_row - 1, center_row + 2):
            for k in range(center_column - 1, center_column + 2):
                list3x3.append(grid[r][k])

        max_list.append(max(list3x3))
        list3x3.clear()

    print(max_list)
    list_result.append(list(max_list))
    max_list.clear()

    center_column = 0

print('result: ')
print(list_result)

