# AND OR NOT
# w jakiej czesci układu współrzędnych znajduje się punkt (x,y)
#
# x = 0
# y = 0
#
# if x > 0:
#     if y > 0:
#         print('part I')
#     elif y > 0:
#         print('part IV')
#     elif y == 0:
#         print('on axis x+')
#     else
#
# # AND
# True  and True  >> True
# True  and False >> False
# False and True  >> False
# False and False >> False
# a and b and c
#
# # OR
# True  or True  >> True
# True  or False >> False
# False or True  >> False
# False or False >> False
# a or b or c
#
# (a and b) or (c and d) or (e and f)

# and zatrzymuje się na fałszu a and b and c and d and e
# or zatrzymuje się na prawdzie a or b or c or d or e


number = int(input('Enter number : '))
if number % 2 == 0:
    print ('Zero')