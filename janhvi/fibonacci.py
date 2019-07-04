num = int(input("Enter the terms in fibonacci series : "))
if num < 0:
    print("Not a valid number!")
else:
    f1 = 0
    f2 = 1
    if num == 1:
        print(f1)
    else:
        print(f1)
        print(f2)
        for i in range(2, num):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            print(f3)

