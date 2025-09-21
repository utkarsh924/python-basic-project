# Menu driven calculator

a=int(input('Entered the 1st number'))
b=int(input('Entered the 2nd number'))

op=input('Entered the operation')

if op== '+' :
    print(a+b)
elif op== '-' :
    print(a-b)
elif op== '*' :
    print(a*b)
else :
    print(a/b)