class NumberUtils:
    def __init__(self, number):
        self.number = number

    def reverse(self):
        reversed_num = 0
        num = self.number
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num = num // 10
        return reversed_num

# Example usage
number = int(input("Enter a number: "))
num_obj = NumberUtils(number)
print("Reversed number:", num_obj.reverse())
