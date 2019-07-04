from math import sqrt
for i in range(1, 500, 1):
    if int(sqrt(i)+0.5) ** 2 == i:
        print(i)
