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
