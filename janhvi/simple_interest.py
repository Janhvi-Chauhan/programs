p = int(input("Enter the Principle amount : "))
r = int(input("Enter the rate of interest (%): "))
t = int(input("Enter the time period (in years): "))
si = (p*r*t)/100
print("Interest = ", si)
print("Amount to pay is : ", si+p)

