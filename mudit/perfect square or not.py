import math 

n = int(input("Enter an number"))
i=int(math.sqrt(n))

if(n==i*i):
  print(" Yeah its a perfect square: %d * %d = %d"%(i,i,n))
else:
  print("Not a perfect square")

input()
