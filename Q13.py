# 13. Write a program that takes an integer as input and checks if it is divisible by 17.

n = int(input("Enter an integer: "))

if(n%17 == 0):
    print(f"{n} is divisible by 17")
else:
    print(f"{n} is not divisible by 17")