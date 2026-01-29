# 2. Write a program that takes two integers a and b as input and prints their sum, difference,
# product, quotient, and remainder.

a = int(input("Enter a integer:"))
b = int(input("Enter other integer:"))
sum = a+b
product = a*b
if(a>b):
    difference = a - b
    quotient = a / b
    remainder = a % b
else:
    difference = b - a
    quotient = b / a
    remainder = b % a

print("Sum = ", sum)
print("Difference = ", difference)
print("Product = ", product)
print("Quotient = ", quotient)
print("Remainder = ", remainder)