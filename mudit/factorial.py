n=int(input("Enter number"))
print("Factorial of the number is")
f=lambda n: n*f(n-1) if n>0 else 1

result=f(n)
print(result)

input()
