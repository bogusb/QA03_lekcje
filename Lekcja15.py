#Lekcja15

# animals = ['dog', 'cat', 'parrot', 'mouse']
# print(animals)
# animals[2] = 'goose'
# print(animals)

# metody = funkcje obiektów, np. metody spiskov

# colors = ['Red', 'Green', 'Blue']
# print(colors)
# colors.append('Orange') # Add to the end of list

# Append to start of list
colors = ['Red', 'Green', 'Blue']
print(colors)
colors = colors[::-1]
print(colors)
colors.append('Orange')
print(colors)
colors = colors[::-1]
print(colors)

colors.insert(2, 'Yellow')

colors.pop()
colors.pop(0)

del colors # to jest funkcja a nie metod
len(colors) # to też jest funkcja

# obiekt hranit ssylku

colors.remove('Green')

real_colors = colors[:]
