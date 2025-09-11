def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return reversed_num

# Example usage
number = int(input("Enter a number: "))
print("Reversed number:", reverse_number(number))
