# Модуль 3. Циклы. Часть 5

# Задание. Вывести на экран фигуры, заполненные звездочками. Диалог с пользователем реализовать при помощи меню.

res_image_1,res_image_2,res_image_3,res_image_4,res_image_5_part_1,res_image_5_part_2,res_image_6,res_image_7,res_image_8,res_image_9,res_image_10 = '','','','','','','','','','',''

for i in range(5):
    res_image_4 += ' ' * 10
    res_image_4 += '\n'

for count in range(1, 11):
    for spaces_1 in range(1, count):
        res_image_1 += ' '
        
    for stars_1 in range(1, -count + 12):
        res_image_1 += '*'
        
    for stars_2 in range(1, count + 1):
        res_image_2 += '*'
    
    for spaces_2 in range(1, -count + 11):
        res_image_2 += ' '

    if count <= 5:
        for stars_6 in range(1, count + 1):
            res_image_6 += '*'
        
        for spaces_6 in range(1, -count + 11):
            res_image_6 += ' '

        for spaces_7 in range(1, -count + 12):
            res_image_7 += ' '
    
        for stars_7 in range(1, count + 1):
            res_image_7 += '*'
    else:
        for stars_6 in range(1, -count + 12):
            res_image_6 += '*'
    
        for spaces_6 in range(1, count):
            res_image_6 += ' '
        
        for spaces_7 in range(1, count + 1):
            res_image_7 += ' '
        
        for stars_7 in range(1, -count + 12):
            res_image_7 += '*'
    

    if count == 2:
        res_image_4 += ' ' * 4
        res_image_5_part_2 += ' ' * 4

    if count == 3:
        res_image_3 += ' '
        res_image_5_part_1 += ' '

    if count == 4:
        res_image_4 += ' ' * 3
        res_image_5_part_2 += ' ' * 3

    if count == 5:
        res_image_3 += ' ' * 2
        res_image_5_part_1 += ' ' * 2

    if count ==6: 
        res_image_4 += ' ' * 2
        res_image_5_part_2 += ' ' * 2

    if count == 7:
        res_image_3 += ' ' * 3
        res_image_5_part_1 += ' ' * 3

    if count == 8:
        res_image_4 += ' '
        res_image_5_part_2 += ' '

    if count == 9:
        res_image_3 += ' ' * 4
        res_image_5_part_1 += ' ' * 4

    for stars_3 in range(1, -count + 12):
        if (-count + 11) % 2 == 0:
            res_image_3 += '*'
            res_image_5_part_1 += '*'
        else:
            break

    for stars_4 in range(count):
        if count % 2 == 0:
            res_image_4 += '*'
            res_image_5_part_2 += '*'
        else:
            break

    if count <= 5:
        for stars_8 in range(1, count + 1):
            res_image_8 += '*'

        for spaces_8 in range(1, -count * 2 + 11):
            res_image_8 += ' '

        for stars_8 in range(1, count + 1):
            res_image_8 += '*'
    else:
        for stars_8 in range(1, -count + 12):
            res_image_8 += '*'

        for spaces_8 in range(1, count * 2 - 11):
            res_image_8 += ' '

        for stars_8 in range(1, -count + 12):
            res_image_8 += '*'

    if count == 2:
        res_image_4 += ' ' * 4
        res_image_5_part_2 += ' ' * 4

    if count == 3:
        res_image_3 += ' '
        res_image_5_part_1 += ' '

    if count == 4:
        res_image_4 += ' ' * 3
        res_image_5_part_2 += ' ' * 3

    if count == 5:
        res_image_3 += ' ' * 2
        res_image_5_part_1 += ' ' * 2

    if count ==6: 
        res_image_4 += ' ' * 2
        res_image_5_part_2 += ' ' * 2

    if count == 7:
        res_image_3 += ' ' * 3
        res_image_5_part_1 += ' ' * 3

    if count == 8:
        res_image_4 += ' '
        res_image_5_part_2 += ' '

    if count == 9:
        res_image_3 += ' ' * 4
        res_image_5_part_1 += ' ' * 4
    
    for stars_9 in range(1, -count + 12):
        res_image_9 += '*'
    
    for spaces_9 in range(1, count):
        res_image_9 += ' '
    
    for spaces_10 in range(1, -count + 12):
        res_image_10 += ' '
    
    for stars_10 in range(1, count + 1):
        res_image_10 += '*'

    res_image_1 += '\n'
    res_image_2 += '\n'
    res_image_3 += '\n' if (-count + 11) % 2 == 0 else ''
    res_image_4 += '\n' if count % 2 == 0 else ''
    res_image_5_part_1 += '\n' if (-count + 11) % 2 == 0 else ''
    res_image_5_part_2 += '\n' if count % 2 == 0 else ''
    res_image_6 += '\n'
    res_image_7 += '\n'
    res_image_8 += '\n'
    res_image_9 += '\n'
    res_image_10 += '\n'

for i in range(5):
    res_image_3 += ' ' * 10
    res_image_3 += '\n'

while True:
    switch_variable_for_image = int(input('Выбор рисунка\nВведите номер рисунка\n(1-10/0 - выйти из программы):'))
    
    if switch_variable_for_image == 1:
        print(res_image_1)   
    elif switch_variable_for_image == 2:
        print(res_image_2)
    elif switch_variable_for_image == 3:
        print(res_image_3)
    elif switch_variable_for_image == 4:
        print(res_image_4)
    elif switch_variable_for_image == 5:
        print(res_image_5_part_1 + res_image_5_part_2)
    elif switch_variable_for_image == 6:
        print(res_image_6)
    elif switch_variable_for_image == 7:
        print(res_image_7)
    elif switch_variable_for_image == 8:
        print(res_image_8)
    elif switch_variable_for_image == 9:
        print(res_image_9)
    elif switch_variable_for_image == 10:
        print(res_image_10)
    else:
        print('Выход из программы')
        break

