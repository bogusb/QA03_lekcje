# Lekcja14

# [20:04] Буйлук Андрей
# Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# Zadanie z gwiazdką *. Bez używania metody count.

# Задание 5
# Zadanie z gwiazdką *. Bez używania metody replace.

# [20:11] Буйлук Андрей
# '''Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# * Без использования метода count'''
# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))
# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.
# * Без использования метода replace'''
# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
#
# print(s)


# metody
# s = 'Abra kadabra'
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.capitalize())

# [20:23] Буйлук Андрей
# '''Задание 1
# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось
# с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в
# тексте.'''

# #[20:26] Буйлук Андрей
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# t = t.capitalize()
# print(t)
#
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# numeric = '0123456789'
# punctuation_mark = '!?.'


# # revers stroki
# s = 'Hello World!'
# print(s[::-1]) # !dlroW olleH
#
# s = 'Hello World!'
# print(s[0:5])#Hello
# print(s[-6:-1])#World
# print(s[-6:])#World!
# print(s[:5])#Hello
# print(s[::-1])#!dlroW olleH


word = 'Hello World!'
print(word.find('l'))
print(word.rfind('l'))

# zapisać sobie w notesiku pytania do lekcji, i potem zadać je.

# [21:28] Соморов Андрей Анатольевич
# # Задание 4
# # Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум
# # и минимум, введенных чисел. Когда пользователь вводит число 7 программа прекращает
# # свою работу и выводит на экран надпись «Good bye!»
# a = int(input('введите число -'))
# mn = a
# mx = a
# c = 0
# while a != 7:
#     c = c + a
#     if a > mx:
#         mx = a
#     elif a < mn:
#         mn = a
#     elif a == 7:
#         print('Good bye!')
#         break
#     a = int(input('введите число -'))
# print('максимум =', mx)
# print('минимум =', mn)
# print('сумма чисел равна:', c)


# [21:34] Черняк Александр Игоревич
# maxn = 0
# minn = 0
# x = int(input("Enter the Number  "))
#
# sum = 0
# while x != 7:
#     if x == 7:
#         print("Good bye!")
#     sum = sum + x
#     if x > maxn:
#         maxn = x
#     elif x < minn:
#         minn = x
#     x = int(input("Enter the Number, or 7 to stop  "))
# print(maxn, minn, sum,"Max, Min, Sum")
#
#  like 1

# Санатарчук Анастасия Игоревна21:22
# 3 razy zadania w obrazkach

number = 123456
str_number = 'aaa' + str(number) + 'qqq'
print(str_number)

# [21:42] Ковалёв Виктор Александрович
# Вопрос об автоматизации.когда реально будет устроится на qaautomatization?
# берут ли джунов в автоматизацию?
# если нет,где набраться опыта и как всё не забыть до того момента?)

