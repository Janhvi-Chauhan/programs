x=int(input("Enter where you want to start"))
y=int(input("Enter where you wnat to end"))
print("The numbers not divisible by 3 or 5 are")
for i in range(x,y):

     if i%3==0 or i%5==0:
         continue

     print(i)
input()
