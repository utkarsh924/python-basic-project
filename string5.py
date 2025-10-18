# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam
# these words are looks like same both side.

user= input('Enter the string:')
flag= True
for i in range (0,len(user)//2):
    if user[i] != user[len(user)-i -1]:
        flag= False
        print('opps! its not a palindrome')
        break
if flag:
        print('yaaho its a palindreme')