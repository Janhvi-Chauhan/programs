def count(l):
    even = 0
    odd = 0
    for j in l:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = []
length = int(input("Enter number of elements in list : "))
for i in range(length):
    val = int(input("value "))
    lst.append(val)
e, o = count(lst)
print("Even = ", e)
print("Odd = ", o)
