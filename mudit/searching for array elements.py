from array import *

arr=array('i',[])
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("Enter the next element"))
    arr.append(x)

print(arr)

k=0
value=int(input("Enter the  element you want to search"))
print("Searched element will have index number")
for e in arr:
     if e==value:
         print(k) 
         break
     k+=1

input()
