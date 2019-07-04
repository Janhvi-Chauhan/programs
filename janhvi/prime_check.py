num = int(input("Enter a Number : "))
for i in range(2, num, 1):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
