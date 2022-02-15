# Lekcja18

# # Objavlenie funkcji
# def hello():
#     print('Hello world!')

# # Vyzov funkcji , Tielo funkcji
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
#
# def hello_name(name):# argumenty, atrybuty, pieriemiennyje funkcji




# [20:18] Буйлук Андрей
# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
#                                 Steve Jobs

# def steve_jobs():
#     print(f'"Don\'t let the noise of others\' opinions\ndrown out your own inner voice."\n                             Steve Jobs')
#
# steve_jobs()

# def odd(a, b): # parametry funkcji
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             print(i)
#
# odd(4, 9)


# [20:39] Буйлук Андрей
# Задание 3
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии,
# направление, символ.
#
# many_symb = 5
# symb = 'W'
#
# def vert_line(many_symb, symb):
#     for i in range(long):
#         print(symb)

# # [20:47] Буйлук Андрей
# def line(length, direction, symbol):
#     s = ''
#     while length > 0:
#
#         if direction == 'horizontal':
#             s = s + symbol
#         elif direction == 'vertical':
#             s = s + '\n' + symbol
#         length = length - 1
#     print(s)


# # [21:01] Буйлук Андрей
# # '''Задание 5
# # Напишите функцию, которая возвращает сумму чисел
# # в указанном диапазоне. Границы диапазона передаются
# # в качестве параметров.'''
#
# start_range = 5
# end_range = 15
#
# def summa(start_range, end_range):
#     summa_range = 0
#     if start_range > end_range:
#         start_range, end_range = end_range, start_range
#     for i in range(start_range, end_range + 1):
#         summa_range = summa_range + i
#     return summa_range
#
# a = summa(13, 12)
# print(a)
#
# [21:13] Буйлук Андрей
# Задание 6
# Напишите функцию, которая проверяет является ли
# число простым. Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе
# false.


def factorisation(n):
    factors = []
    k = 2
    while n != 1:
        while n % k == 0:
            n = n // k
            factors.append(k)
        k = k + 1
    # f = (len(factors) == 1)
    return factors

# a = factorisation(6)
# print(a)


# # [21:25] Буйлук Андрей
def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# for i in range(2, 10000000000000000000):
i = int(input("Wprowadź liczbę :  "))
print(i, ': ', factorisation(i))
# print(i, ': ', simple(i))

input()