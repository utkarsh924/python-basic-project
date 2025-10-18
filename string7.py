# Write a python program to conver a string to title cas without using the title()

user= input('Enter the title:')
L = []

for i in user.split():
  L.append(i[0].upper() + i[1:].lower())
print(L)