a=(input("Enter first city or any name"))
b=(input("Enter second city or name"))
c=(input("Enter third city or any name"))

print("In dictionary the list would be")
if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
else:
    print(c,b,a)

input()
