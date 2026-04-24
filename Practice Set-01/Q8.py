# 8. Write a program that takes a three-digit integer as input and prints the sum of its digits.

a = int(input("Enter an three digit integer: "))

temp1 = a%10
a = a//10
temp2 = a%10
a = a//10
temp3 = a%10

sum = temp1 + temp2 + temp3
print(sum)