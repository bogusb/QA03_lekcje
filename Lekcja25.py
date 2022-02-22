# #Lekcja25
# # primes
# def is_prime(integer):
#     if 1 < integer:
#         for i in range(2, integer):
#             if integer % i == 0:
#                 return False
#         return True
#
#
# def number_of_primes(list_of_integers):
#     number_of_prim = 0
#     for element in list_of_integers:
#         if is_prime(element) is True:
#             number_of_prim = number_of_prim + 1
#     return number_of_prim
#
#
# a = number_of_primes([2, 5, 4, -11, 137, -2, 2, 1, 0, 3])
# print(a)  # 5

#
# # ----------------------------------------
# # Задание 1:
# # Пользователь вводит с клавиатуры арифметическое
# # выражение. Например, 23+12.
# # Необходимо вывести на экран результат выражения.
# # В нашем примере это 35. Арифметическое выражение
# # может состоять только из трёх частей: число, операция,
# # число. Возможные операции: +, -,*,/
# #
# # Variables
# expression_entered = ''
# component = ''
# components = []
# result = 0
#
# # Enter data
# expression_entered = str(input("Enter an arithmetic expression (e.g. 23+12) :  "))
# # expression_entered = '12.45678 + 237'
# # expression_entered = '12/3'
# # expression_entered = ' - '   -3-3 nie pracuje!!!
#
# # Order data
# for i in expression_entered:
#     if i.isnumeric() is True or i == '.':
#         component = component + i
#     elif i == '+' or i == '-' or i == '*' or i == '/':
#         components.append(component)  # 1st component
#         components.append(i)  # +-*/
#         component = ''
#
# components.append(component)  # 2nd component
#
# # Final result
# # print(components)
# if components[0] == '':
#     components[0] = '0'
# if components[2] == '':
#     components[2] = '0'
#
# expression_entered = components[0] + ' ' +  components[1] + ' ' +  components[2] + '  =  '
# components[0] = float(components[0])
# components[2] = float(components[2])
#
# if components[1] == '+':
#     result = (components[0] + components[2])
# elif components[1] == '-':
#     result = (components[0] - components[2])
# elif components[1] == '*':
#     result = (components[0] * components[2])
# elif components[1] == '/':
#     if components[2] != 0:
#         result = (components[0] / components[2])
#     else:
#         expression_entered = expression_entered + 'Divide by zero!  '
#
# if float(result) != int(float(result)):
#     result = float(result)
# else:
#     result = int(result)
#
# print(expression_entered, result)
#
# input()
#



###
### OOP    Programowanie zOrientowane Obiektowo
# ###
# # wszystko jest obiektem int, str to gotowe obiekty z Pythona
#
# a = int(5)
# b = str('Hello')
# c = list([1,2,3])
#
# # filiżanka to też obiekt, który jest w wielu domach
# # wy sami tworzycie obiekty i nadajecie swoje zasady
# # 2 + 2 = 5
#
# # class to instrukcja obiektu, przepis na barszcz, jego zjeść nie mogę
#
# class Box:
#     v = 5  # argument klassa, atrybut klassa, pole klassa, field, pieriemienna klassa
#     # parametry klassa: co? ile? jaki? gdzie? życie, waga, tank
#     def open(self, count):  # self = ja, to metod a nie funkcja. metod klassa, method, funkcja klassa
#         print(f'Open {count} box')
#
# lanch = Box()
# print(lanch.v)
# lanch.open(2)
#
# tools = Box()
# tools.open(5)

class Borsch:
    volume = 3
    color = 'red'
    components = ['Beetroot', 'Tomato', 'Meat', 'Potato']
    temperature = 20.5
    vegetarian = False
    create_date = '22/02/2022'
    life_period = 480
    def heating(self):
        self.temperature = self.temperature + 5
    def show_heating(self):
        return self.temperature
    def more_borsch(self):
        self.volume = self.volume + 1
    def show_volume(self):
        return self.volume
    def change_color(self, new_color):
        self.color = new_color



andrii_borsch = Borsch()  # tworzy obiekt klassa Borsch
print(andrii_borsch.show_heating())
andrii_borsch.heating()
andrii_borsch.heating()
print(andrii_borsch.show_heating())
print(andrii_borsch.show_volume())
andrii_borsch.more_borsch()
andrii_borsch.more_borsch()
print(andrii_borsch.show_volume())


sten_borsch = Borsch()
sten_borsch.color = 'green'

print(andrii_borsch.color)
print(sten_borsch.color)
andrii_borsch.change_color('yellow')
print(andrii_borsch.color)
print(sten_borsch.color)

