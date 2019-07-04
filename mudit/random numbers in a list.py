import random
a=[]
n=int(input("Enter number of elements:"))
x=int(input("Enter lower limit"))
y=int(input("Enter upper limit"))
print("The random numbers in the list wiil be")
for j in range(n):
  
    a.append(random.randint(x,y))

print("Randomised list is:" ,a)

input()
