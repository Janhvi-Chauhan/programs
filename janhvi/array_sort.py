from array import *
arr = array('i', [])
length = int(input("Enter the length of the Array : "))
for i in range(length):
    val = int(input("Value : "))
    arr.append(val)
print("Initial Array Was : ", arr)
print("Sorted Array Is : ", sorted(arr))

