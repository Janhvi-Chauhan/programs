n=int(input("Enter any numbers:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number.")
else:
    print("The number is not armstrong number.")

input()    