def check(n):
    c = 0
    for i in n:
        if i > 5:
            c += 1
    return c


name = []
length = []
for j in range(10):
    x = input("Enter Name : ")
    count = len(x)
    length.append(count)
    name.append(x)
num = check(length)
print(num, "names have more than 5 characters.")
