# 5. Write a program that takes an integer as input, and displays whether this integer is negative,
# positive, or zero.

n = int(input("Enter an integer: "))

if(n > 0):
    print(f"{n} is positive integer")
elif(n < 0):
    print(f"{n} is negative integer")
else:
    print(f"{n} is zero")