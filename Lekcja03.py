# Lekcja03
# if...elif...else
# print(2+2)
# print(2/4)

# Matematyczne

# Logiczne > < >= <= == !=
# print(5>2)
# print(4<4)
#
# age = 13 #PEP 8 CISCO
# if age < 18:#True
#     print('Child')
# if age > 18:#False
#     print('Adult')

# age = 18
# if age < 18:
#     print('Child')
# if age >= 18:
#     print('Adult')

# age = 18
# if age < 18:
#     print('Child')
# else:
#     print('Adult')

# weight = 120
# if weight < 150:
#     print(weight)
# else:
#     print('Weight > MAX')
#
# age = 15
# if age < 0:
#     print('Error-')
# elif age < 13:#else if
#     print('Child')
# elif age < 18:#else if
#     print('Teen')
# elif age < 135:#else if
#     print('Adult')
# else:
#     print('Error+')
# print("*END*")
# print(type(age))
#try...except...else...finally Lesson23

# if type(weight) != type(1)


weight = 1100
if (weight <= 0):
    print('Too tiny')
elif (weight < 20):
    print('You child')
elif (weight < 100):
    print('You healthy!')
elif (weight < 150):
    print('Enough!')
elif (weight < 1000):
    print('Do not eat Mac!')
else:
    print('Overdose')