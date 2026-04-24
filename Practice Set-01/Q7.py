# 7. Write a program that takes three integers as input and prints their maximum value.

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if(a>b and a>c):
    print("a is maximum")
elif(b>a and b>c):
    print("b is maximum")
else:
    print("c is maximum")