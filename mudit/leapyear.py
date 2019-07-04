x=int(input("Enter an year"))
result= "Leap Year" if x%400==0 else "Leap Year" if x%4==0 and x%100!=0 else "Non Leap Year"
print(result)
input()
