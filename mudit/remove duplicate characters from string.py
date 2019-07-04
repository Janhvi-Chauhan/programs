s=input("Enter a string")
print("The string after removing duplicate characters will be")
i=0
s1=""
for x in s:
    if s.index(x)==i:
        s1+=x
    i+=1
print(s1)

input()
