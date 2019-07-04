from array import *
arr = array('i', [])
length = int(input("Enter the length of the Array : "))
for i in range(length):
    val = int(input("Value : "))
    arr.append(val)
search = int(input("Enter the value whose index is to be searched : "))
for i in range(length):
    if search == arr[i]:
        print("Number found at index ", i)
        break
else:
    print("Number not found")
