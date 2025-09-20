#Program - Find the sum of a 3 digit number entered by the user
number=int(input("Enter the 3 digit number"))


# 345 %10 ->5
a=number%10
number=number//10

# 45 % 10 ->4
b=number%10
number=number//10

# 3 % 10 ->3
c=number%10
print(a+b+c)

