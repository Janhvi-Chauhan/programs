l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
print("The perfect squares in this  range is")
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x]
print(a)

input()