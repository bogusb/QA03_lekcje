# # str metody strok łańcuchy znaków
# # iteriruemyj perebierajemyj\ nie izmieniajemyj typ dannyh\ indeksirujemyj
# h = 'Hello World!'
# #    0123456789
# print(h)
# print(h[0])
# h = h + '?'
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[3])

# n = 'Barszcz Boguslaw Francevich'
# print(n[17], n[18], n[22], n[20], n[21], n[26]) # F r e n ch
# print(n[0], n[11], n[4], n[6]) # B u z z
# print(n[0], n[0], n[0], n[0], n[0])


# '''Задание 1
# Пользователь вводит с клавиатуры строку.
# Произведите поворот строк и полученный результат выведите
# на экран.'''

# s = 'Hello World!'
# # variant 1
# rs = ''
# for i in range(len(s)):
#     rs = s[i] + rs
# print(rs)


# [19:17] Буйлук Андрей

# '''Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв,
# цифр в строке. Выведите оба
# количества на экран.'''

# letters = 'abcdefghijklmnopqrstuvxyz'
# numbers = '0123456789'
# symbols = '!@#$%^&*()_+='
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letters = count_letters + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
# print(count_numbers, count_letters)

# python string metod
#
# w Europie GDPR standard, hasła nie podglądacie, a sprawdzacie,
# czy ma cyfry, czy ma symbole, czy ma litery małe, czy ma litery duże

# symbol - to nie cyfra i nie litera


# [19:36] Буйлук Андрей
# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

s = 'Abrakadabra'
symbol_find = 'd'
# count = 0

# for i in range(len(s)):
#     if s[i] == symbol_find:
#         count = count + 1
# print(count) # 2

symbol_find = 'ra'
print(s.count(symbol_find)) # metod .count jak Frameworki szybko działają bo napisane w C++
