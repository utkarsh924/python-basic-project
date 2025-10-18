# Write a program which can remove a particular character from a string.

user= input('Enter the string:')

term= input('what would you like to remove')

result= ''

for i in user:
    if i != term:
        result= result+i
print(result)

