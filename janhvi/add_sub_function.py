def add_sub(num1, num2):
    total = num1 + num2
    if num1 > num2:
        diff = num1 - num2
    else:
        diff = num2-num1
    return total, diff


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
a, b = add_sub(x, y)
print("Sum of the numbers is : ", a, "\nDifference between the numbers is : ", b)
