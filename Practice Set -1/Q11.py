# 11. Write a program that takes an integer as input and displays if it is odd or even.

n = int(input("Enter an integer: "))

if(n%2 == 0):
    print(f"{n} is even")
else:
    print(f"{n} is odd")