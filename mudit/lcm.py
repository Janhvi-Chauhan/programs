a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("The LCM of the numbers will be")

if(a>b):
    min=b
else:
    min=a
while(1):
    if(min%a==0 and min%b==0):
        print("LCM is:",min)
        break
    min=min+1

input()
