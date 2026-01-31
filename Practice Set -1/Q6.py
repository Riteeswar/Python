# 6. Write a program that takes two integers a and b as input and displays whether a < b, a = b,
# or a > b.

a = int(input("Enter an integer: "))
b = int(input("Enter other integer: "))

if(a < b):
    print("a is less than b")
elif(a > b):
    print("a is greater than b")
else:
    print("a is equal to b")