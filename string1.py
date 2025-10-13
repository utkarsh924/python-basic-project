# Find the length of a given string without using the len() function

text= input('Enter the string:')
counter= 0

for i in text:
    counter += 1
print('length of string',counter)