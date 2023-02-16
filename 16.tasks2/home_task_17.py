# 1.

# Дан массив целых чисел,
# отсортируйте массив в порядке
# возрастания в зависимости от
# частоты значений.
#
# Вернуть отсортированный массив.
#
# lst = [2, 1, 2, 2, 1, 3] => [3, 1, 1, 2, 2, 2]

lst = [2, 1, 2, 2, 1, 3]
# print(min(lst))

min_int = min(lst)
max_int = max(lst)
count_int = []
result = []

while min_int <= max_int:
    count_int.append(lst.count(min_int))
    min_int += 1

count_int.sort()

for i in range(len(count_int)):
    for j in lst:
        if count_int[i] == lst.count(j):
            result.append(j)

print('Задача 1')
print(result)

# 2.

# Вам дан массив nums, состоящий
# из целых положительных чисел.
#
# Вы должны взять каждое целое число
# в массиве, поменять местами его цифры
# и добавить новое число в конец массива.
#
# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.


# Решение, как я понял условие задачи:
nums = [112,13,32,601,513,513]

def reverse_digit_and_add_to_end(nums_list):
    nums = nums_list
    for i in range(len(nums_list)):
        nums.append(int(str(nums_list[i])[::-1]))

    return nums


def get_unique_numbers(nums_list, sz):
    nums = reverse_digit_and_add_to_end(nums_list)
    end_list = []
    result = []

    for i in range(sz):
        end_list.append(nums[-(i + 1)])

    for j in range(len(end_list)):
        if end_list.count(end_list[j]) == 1:
            result.append(end_list[j])
    
    return result

print('Задача 2')
sz = len(nums)
print(get_unique_numbers(nums, sz))
# 3.

# Дан массив целых чисел nums.
# Верните максимальное значение такое, что:
# (nums[i]-1)*(nums[j]-1).

nums = [1,2,3,4,5,4,3,2,6,7,8,9]
nums.sort()
max1 = nums[-1]
max2 = nums[-2]
print('Задача 3')
print((max1 - 1) * (max2 - 1))