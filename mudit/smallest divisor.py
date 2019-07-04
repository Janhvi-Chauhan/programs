n=int(input("Enter an integer"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)


print("Smallest divisor is:",a[0])

input()
