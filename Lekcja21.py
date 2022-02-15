# Lekcja21
# Files Pliki
import random
import time

#IDE

# f = open('test.txt', 'wt') # t - text / b - binary     w - write   r - read
# # open ('fff', 'rt')
# f.write('My name is Sten, Bob')
# # time.sleep(15)
# f.close()
# # random.randint()
# f = open('test.txt', 'rt')
# print(f.read()) # zczytuje plik w całości
# f.close()
#
# #w - write otkryt' fajl na zapis
# #r - read otkryt' fajl na cztenije
#
# f = open ('test.txt', 'rt')
# print(f.readline())# zczytuje fajl postroczno, kak iterirujemyj obiekt
# print(f.readline())
# print(f.readline())
# f.close()

f = open ('test.txt', 'rt')
print(f.readlines())# zczytuje fajl w całości, kak spisok
f.close()

#w - write  /pierezapisat'
f = open ('test.txt', 'wt')
f.write('My name is Andrey\nHow are you?\n')

f.close()

# a - add
f = open ('test.txt', 'at')

# x - add
f = open ('test.txt', 'xt')


[19:40] Буйлук Андрей
import random
f = open('numbers.txt','wt')
for i in range(10):
    for j in range(10):
        f.write(str(random.randint(1,9)))
    f.write('\n')
f.close()

[19:46] Буйлук Андрей
n1 = open('numbers1.txt','rt')
n2 = open('numbers2.txt','rt')
n3 = open('numbers3.txt','wt')
ln1 = n1.readline()
ln2 = n2.readline()
while ln1 or ln2:
    n3.write(ln1)
    n3.write(ln2)
    ln1 = n1.readline()
    ln2 = n2.readline()
n3.close()

# file = open("text.txt", "w")
# file.write("Your text goes here")
# file.close()
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists