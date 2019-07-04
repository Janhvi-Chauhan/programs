from array import *
arr1 = array('i', [])
length1 = int(input("Enter the length of the Array 1 : "))
for i in range(length1):
    val = int(input("Value : "))
    arr1.append(val)
arr2 = array('i', [])
length2 = int(input("Enter the length of the Array 2 : "))
for i in range(length2):
    val = int(input("Value : "))
    arr2.append(val)
result = array('i', [])
if length1 == length2:
    for i in range(length2):
        result.append(arr1[i]+arr2[i])
    print(result)
else:
    print("Arrays must be of equal length")
