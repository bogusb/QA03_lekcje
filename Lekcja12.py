# # Lekcja12 Kolko i krzyzyk
# # Tic Tac Toe
#
# # Variables
# player1_symbol = 'X'
# player2_symbol = 'O'
# player1_choice = '0'
# player2_choice = '0'
#
# board_1 = '1'
# board_2 = '2'
# board_3 = '3'
# board_4 = '4'
# board_5 = '5'
# board_6 = '6'
# board_7 = '7'
# board_8 = '8'
# board_9 = '9'
# turn = 'X'
#
# # # Show board (simple)
# # print(board_1, board_2, board_3)
# # print(board_4, board_5, board_6)
# # print(board_7, board_8, board_9)
#
# # Show board (pro)
# # board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
# board = f'{board_1}|{board_2}|{board_3}\n{board_4}|{board_5}|{board_6}\n{board_7}|{board_8}|{board_9}'
# print(board)
#
# # Game choice
# player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
#

#[20:58] Буйлук Андрей
#Крестики Нолики
#Tic Tac Toe
#Variables
player1_symbol = 'X'
player2_symbol = 'O'
player1_choice = '0'
player2_choice = '0'
board_1 = '1'
board_2 = '2'
board_3 = '3'
board_4 = '4'
board_5 = '5'
board_6 = '6'
board_7 = '7'
board_8 = '8'
board_9 = '9'
turn = 'X'
#Show board (simple)
# print(board_1,board_2,board_3)
# print(board_4,board_5,board_6)
# print(board_7,board_8,board_9)

for i in range(5):
    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    while True:
        #Game choice
        player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
        #Board update
        if player1_choice == board_1:
            board_1 = player1_symbol
            break
        elif player1_choice == board_2:
            board_2 = player1_symbol
            break
        elif player1_choice == board_3:
            board_3 = player1_symbol
            break
        elif player1_choice == board_4:
            board_4 = player1_symbol
            break
        elif player1_choice == board_5:
            board_5 = player1_symbol
            break
        elif player1_choice == board_6:
            board_6 = player1_symbol
            break
        elif player1_choice == board_7:
            board_7 = player1_symbol
            break
        elif player1_choice == board_8:
            board_8 = player1_symbol
            break
        elif player1_choice == board_9:
            board_9 = player1_symbol
            break

    #Show board (pro)
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    while True:
        #Game choice
        player2_choice = str(input(f'Enter your choice {player2_symbol}: '))
        #Board update
        if player2_choice == board_1:
            board_1 = player2_symbol
            break
        elif player2_choice == board_2:
            board_2 = player2_symbol
            break
        elif player2_choice == board_3:
            board_3 = player2_symbol
            break
        elif player2_choice == board_4:
            board_4 = player2_symbol
            break
        elif player2_choice == board_5:
            board_5 = player2_symbol
            break
        elif player2_choice == board_6:
            board_6 = player2_symbol
            break
        elif player2_choice == board_7:
            board_7 = player2_symbol
            break
        elif player2_choice == board_8:
            board_8 = player2_symbol
            break
        elif player2_choice == board_9:
            board_9 = player2_symbol
            break


