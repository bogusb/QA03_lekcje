# Lekcja10
'''[20:37] Буйлук Андрей
Задание 3
Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7.

'''
#
# a = 1
# b = 7
# guess = 4
#
# if a <= guess and guess <= b:
#     for i in range (a, b + 1):
#         if i == guess:
#             print('!', i, '!', sep='', end=' ')
#         else:
#             print(i, end=' ')



'''[20:47] Буйлук Андрей
Задание 1
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру.
Например, если пользователь ввёл 3 на экране будет
выведено:
***
***
***
'''
#
# square_of = 4
# for i in range(square_of):
#     print('*' * square_of)


'''[21:02] Буйлук Андрей
Задание 2
Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
заполненный прямоугольник с указанными высотой и
шириной. Например, если пользователь ввёл высоту 3,
а ширину 5 на экране будет выведено:
*****
*****
*****

'''
# height_of_rectangle = 3
# width_of_rectangle = 5
#
# for i in range(height_of_rectangle):
#     print('*' * width_of_rectangle)


'''Задание 3
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
Размер стороны равен введённому размеру.'''

# square_of = 6
# print('*' * square_of)
#
# for i in range(square_of-2):
#     print('*',' ' * (square_of-2), '*', sep='')
#
# print('*' * square_of)


########### drugie rozwiazanie

# width_of = 7
# height_of = 7
# symbol = '#'
# space = ' '
#
# for i in range (height_of):
#     if i == 0 or i == (height_of -1):
#         print(symbol * width_of)
#     else:
#         print(symbol + (space * (width_of - 2)) + symbol)
