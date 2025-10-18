# count the frequency of a particular character in a provided string.
# eg 'hello how are you' is the string, then the frequency of h in this string is 2.

user= input('Enter the string:')

term= input('what would you like to search for')

counter= 0
for i in user:
    if i== term:
        counter=+ 1
print('frequency',counter)