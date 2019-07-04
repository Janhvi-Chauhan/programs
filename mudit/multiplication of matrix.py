from numpy import *

m1 = matrix('1 2 3; 5 3 1; 4 2 3')

print(m1)
print()

m2 = matrix('3 4 1; 2 6 1; 5 7 8')

print(m2)

print("Sum of the two matrix is:")
print()

def sum():
   
   return(m1+m2)

result=sum()

print(result)
print()


print("Multiplication of the two matrix is:")
print()

m4=m1*m2
print()

print(m4)

input()
