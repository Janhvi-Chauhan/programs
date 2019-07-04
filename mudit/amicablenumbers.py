'''
If we take two numbers and the sum of proper divisors
 of the two numbers is equal to the opposite numbers
then these two numbers are called amicable numbers
'''


x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j

if(sum1==y and sum2==x):
    print("They are Amicable numbers")
else:
    print("They are not amicable")

input()
