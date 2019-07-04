from numpy import *
from array import *

arr1=array('i',[])
n1=int(input("Enter the length of the array"))
for i in range(n1):
    x=int(input("Enter the next element"))
    arr1.append(x)
print(arr1)

arr2=array('i',[])
n2=int(input("Enter the length of the array"))
for e in range(n2):
    y=int(input("Enter the next element"))
    arr2.append(y)
print(arr2)

arr3=arr1+arr2
print("The array after concatenation")
print(arr3)

input()


