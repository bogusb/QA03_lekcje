# Lekcja11   # Rock Paper Scissors

# zadania [18:34] Буйлук Андрей
# Практическое задание:(сделайте как можно больше за 30 минут)

# --------------------------------------------------------
# zad. 1.
# Напишите программу, которая получает длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.

# --------------------------------------------------------
# zad. 2.
# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов.

# --------------------------------------------------------
# zad. 3.
# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

# --------------------------------------------------------
# zad. 4.
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = 2000#int(input("Enter any year (> 1582) : "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0 :
#             print('YES')
#         else:
#             print('NO')
#     else:
#         print('YES')
# else:
#     print('NO')

# # [27.01.2022 19: 27] Barszcz Boguslaw
# # zad. 4.
# # Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# # Если год является високосным, то выведите YES, иначе выведите NO.
# # Напомним, что в соответствии с григорианским календарем, год является високосным,
# # если его номер кратен 4, но не кратен 100, а также если он кратен 400.
#
# year = 1700  # int(input("Enter any year (> 1582) : "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('YES')
#         else:
#             print('NO')
#     else:
#         print('YES')
# else:
#     print('NO')

# --------------------------------------------
# kamień        rock [r]
# papier        paper [p]
# nożyce        scissors [s]


# Rock Paper Scissors

# # [19:34] Буйлук Андрей
# if player1_choice == player2_choice:
#     print('Draw round')
# elif player1_choice == 'r':
#     if player2_choice == 's':
#         print('Player 1 win the round!')
#         player1_score = player1_score + 1
#     else:
#         print('Player 2 win the round!')
#         player2_score = player2_score + 1

# ###
# [19:39] Буйлук Андрей
# #Variables
# player1_score = 0
# player2_score = 0
# player1_choice = ''
# player2_choice = ''
# rounds = 3
# #Start of game
# for i in range(1,rounds+1):
#     #Enter data
#     player1_choice = str(input("Enter your choice player 1: [r],[p],[s] : "))#r
#     player2_choice = str(input("Enter your choice player 2: [r],[p],[s] : "))#p
#     #Compare data
#     # if player1_choice == 'r':
#     #     if player2_choice == 's':
#     #         print('Player 1 win the round!')
#     #         player1_score = player1_score + 1
#     #     elif player2_choice == 'p':
#     #         print('Player 2 win the round!')
#     #         player2_score = player2_score + 1
#     #     else:
#     #         print('Draw round')
#     if player1_choice == player2_choice:
#         print('Draw round')
#     elif player1_choice == 'r':
#         if player2_choice == 's':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
#     elif player1_choice == 'p':
#         if player2_choice == 'r':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
#     elif player1_choice == 's':
#         if player2_choice == 'p':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
# #Compare score
# if player1_score > player2_score:
#     print('Player 1 win the game!')
# elif player2_score > player1_score:
#     print('Player 2 win the game!')
# else:
#     print('Draw game!')
#


### dodatkowo zagrac jeszcze raz
#   provierki zrobic
# 20:21 domaszne zadanie mowi o tym
# 2 graczy tylko bo nie wiadomo kto zwyciezyl
# czy sa jakies idee
# to co zavernute
# player protiv boota, robota, bo tak widzimy ruchy drugiego
# game_type = pvp person vs person    pve person vs boot
#

# # [19:39] Буйлук Андрей
# #Variables
# player1_score = 0
# player2_score = 0
# player1_choice = ''
# player2_choice = ''
# rounds = 3
# #Start of game
# for i in range(1,rounds+1):
#     #Enter data
#     while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's':
#         player1_choice = str(input("Enter your choice player 1: [r],[p],[s] : "))#r
#         print(player1_choice)
#         #    player2_choice = str(input("Enter your choice player 2: [r],[p],[s] : "))#p
    #Compare data
    # if player1_choice == 'r':
    #     if player2_choice == 's':
    #         print('Player 1 win the round!')
    #         player1_score = player1_score + 1
    #     elif player2_choice == 'p':
    #         print('Player 2 win the round!')
    #         player2_score = player2_score + 1
    #     else:
    #         print('Draw round')
#     if player1_choice == player2_choice:
#         print('Draw round')
#     elif player1_choice == 'r':
#         if player2_choice == 's':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
#     elif player1_choice == 'p':
#         if player2_choice == 'r':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
#     elif player1_choice == 's':
#         if player2_choice == 'p':
#             print('Player 1 win the round!')
#             player1_score = player1_score + 1
#         else:
#             print('Player 2 win the round!')
#             player2_score = player2_score + 1
# #Compare score
# if player1_score > player2_score:
#     print('Player 1 win the game!')
# elif player2_score > player1_score:
#     print('Player 2 win the game!')
# else:
#     print('Draw game!')
#
