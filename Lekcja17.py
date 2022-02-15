# Буйлук Андрей18:54# without if (dict)
# n1 = 12
# command = '-'
# n2 = 2
# calc = {'+': n1 + n2, '-': n1 - n2}
# print(calc[command])

# # [18:57] Буйлук Андрей
# l2 = [[1,2,3,4],[4,5,6],[7,8,9]]
# print(l2)
# for i in range(len(l2)):
#     for j in range(len(l2[i])):
#         print(l2[i][j],end=' ')
#     print()
#
# # print(l2[0][0], l2[1][0], l2[2][0])
#
# [19:15] Буйлук Андрей
# tictactoe_board = [[1,2,3],[4,5,6],[7,8,9]]
# for y in range(9):
#     turn = int(input("Enter number of cell: "))
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             if tictactoe_board[i][j] == turn:
#                 tictactoe_board = 'X'

# [19:18] Буйлук Андрей
tictactoe_board = [[1,2,3],[4,5,6],[7,8,9]]
for y in range(9):
    turn = int(input("Enter number of cell: "))
    for i in range(len(tictactoe_board)):
        for j in range(len(tictactoe_board[i])):
            if tictactoe_board[i][j] == turn:
                tictactoe_board[i][j] = 'X'
    for i in range(len(tictactoe_board)):
        for j in range(len(tictactoe_board[i])):
            print(tictactoe_board[i][j], end=' ')
        print()

