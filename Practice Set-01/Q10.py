# 10. Write a program that takes three integers as input and prints the minimum (of the three
# values).

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a<b and a<c):
    print(f"{a} is minimum")
elif(b<a and b<c):
    print(f"{b} is minimum")
else:
    print(f"{c} is minimum")