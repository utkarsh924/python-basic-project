# 1/1!+2/2!+3/3!+............




n = int(input('enter n'))
result = 0
fact = 1
for i in range(1,n+1):
    fact = fact*1
    result = result+ i/fact

print(result)
