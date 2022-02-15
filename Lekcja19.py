#Lekcja19
# [19:12] Буйлук Андрей
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#     else:
#         while 0 < start:
#             numbers.append(start)
#             start = start + 1
#  like 1 star 1


#
# [19:28] Гульшін Олександр Владиславович
# def lucky_num(a):
#     n1 = (a) // 100000
#     n2 = ((a) // 10000) % 10
#     n3 = ((a) // 1000) % 10
#     n4 = ((a) // 100) % 10
#     n5 = ((a) // 10) % 10
#     n6 = ((a) // 1) % 10
#     if n1 + n2 + n3 == n4 + n5 + n6:
#         print("Your number is lucky!")
#         return True
#     else:
#         print("Your number is unlucky!")
#         return False
# print(lucky_num(123420))
#  like 1



# [19:17] Буйлук Андрей
# Задание 7
# Напишите функцию, которая проверяет является
# ли шестизначное число «счастливым». Число передаётся в качестве параметра.
# Если число счастливое нужно вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр
# равна сумме трёх вторых цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
# а 723422 – несчастливое 7+2+3 != 4+2+2.


def lucky6(number):
    for i in number:
        if i.isnumeric():
            if i a = a + i
