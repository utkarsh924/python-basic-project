# Enter the three different numbers 
# and also compare which one is smallest


num1=int(input('Entered the first num'))
num2=int(input('Entered the second number'))
num3=int(input('Entered the third number'))

if num1<num2 and num1<num3 :
    print('smallest is', num1)
elif num2<num3 :
    print('smallest is', num2)
else:
    print('smallest is', num3)