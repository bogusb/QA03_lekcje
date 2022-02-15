#Lekcja20

# # [20:10] Буйлук Андрей
# def average(*numbers):
#     count = len(numbers)
#     sum = 0
#     for number in numbers:
#         sum = sum + number
#     return sum/count
#
#
# print(average(1))  # ,2,3,4,5,6,7,8,9,0,2,4,5))


# [20:20] Буйлук Андрей
# https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html
# Функции и их аргументы | Python 3 для начинающих и чайников
# Именные и анонимные функции, инструкции def, return и lambda, функции с переменным числом аргументов, необязательные аргументы.
#
# [20:21] Буйлук Андрей
# Задание 1
# Написать рекурсивную функцию нахождения степени
# числа.
# Задание 2
# Написать рекурсивную функцию, которая вычисляет
# сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b. Проиллюстрируйте работу функции примером.
# Задание 3
# Написать рекурсивную функцию, которая выводит N
# звезд в ряд, число N задает пользователь. Проиллюстрируйте работу функции примером.
# Задание 4
# Написать игру «Крестики-нолики».
# Задание 5
# Напишите рекурсивную функцию, которая принимает список из 100 целых чисел, полученных случайным
# образом, и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.


# [21:22] Буйлук Андрей
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
# print(factorial(6))


# ----------------------------------------
# [21:35] Швец Людмила Андреевна
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.
#


# ---------------------------------------

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# #Вариант работает при точном совпадении регистра
# ​
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
# ​
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
# ​
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# for word in word_list:
# 	if word in text:
# 		text = text.replace(word,word.upper())
# print(text)
# ​
# #Не чувствителен к регистру, но обратите внимание, что воздействует только на "чистые слова", самое последнее слова, является один целым с точкой, потому его не меняет
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
# ​
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
# ​
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# text_list = text.split(' ')
# for i in range(len(word_list)):
# 		for j in range(len(text_list)):
# 				if word_list[i].lower() == text_list[j].lower():
# 						text_list[j] = text_list[j].upper()
# upper_text = ''
# for text_word in text_list:
# 		upper_text = upper_text + ' ' + text_word
# print(upper_text)


# -------------------------------------------
# mytext = "Python is the best language!"
# mytext_temp = mytext.lower()
# listold = list(mytext.split())
# listnew = list(mytext_temp.split())
# word = ["Python", "is", "best"]
# for i in range(len(listnew)) :
#     print(listnew[i])
#     for j in word :
#
#         if j in listnew[i] :
#             listold[i] = listnew[i].upper()
# print(' '.join(listold))


# -------------------------------------

# [21:46] Гульшін Олександр Владиславович
# Два списка целых заполняются случайными числами.
# # Необходимо:
# # ■ Сформировать третий список, содержащий элементы обоих списков;
# # ■ Сформировать третий список, содержащий элементы обоих списков без повторений;
# # ■ Сформировать третий список, содержащий элементы общие для двух списков;
# # ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# # ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.


